/** @odoo-module **/

import { registry } from "@web/core/registry";
import { CharField } from "@web/views/fields/char/char_field";
import { useService } from "@web/core/utils/hooks";
import { Component, onMounted } from "@odoo/owl";

export class CopyToClipboardField extends CharField {
    setup() {
        super.setup();
        this.notification = useService("notification");
        onMounted(() => {
            const button = this.el.querySelector('.o_copy_clipboard');
            if (button) {
                button.addEventListener('click', () => this.copyToClipboard());
            }
        });
    }

    copyToClipboard() {
        const value = this.props.value;
        if (value) {
            navigator.clipboard.writeText(value).then(() => {
                this.notification.add(this.env._t("Copied to clipboard: ") + value, {
                    type: "success",
                });
            }).catch(() => {
                this.notification.add(this.env._t("Failed to copy"), {
                    type: "danger",
                });
            });
        }
    }

    get isReadonly() {
        return true; // Only enable in read mode
    }
}

CopyToClipboardField.template = "bizzappdev_assignment.CopyToClipboardWidgetTemplate";
registry.category("fields").add("copy_to_clipboard", CopyToClipboardField);

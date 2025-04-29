# Odoo Module: BizzAppDev Solutions Pvt. Ltd.

**Developed by: Jasmin Hirani**

[![Odoo Version](https://img.shields.io/badge/Odoo-18.0-blue.svg)](https://www.odoo.com)  

## Overview

This Odoo module enhances the partner search functionality and improves the delivery order management process, addressing specific requirements outlined in the BizzAppDev Systems Pvt. Ltd. technical assignment.  It includes features for partner reference search, tag synchronization from sales orders to delivery orders, manufacturing order quantity locking, purchase order splitting based on category, automated email notifications, unique category names, a clipboard copy widget, and a modified default search filter.

## Key Features

*   **Enhanced Partner Search:**
    *   Allows searching for partners using the "Ref" field from all Many2one widgets related to the Partner model.
    *   Displays partner names in Many2one fields with the format "PARTNER NAME [REF]" for easy identification.

*   **Sales Order to Delivery Order Tag Synchronization:**
    *   Automatically copies all tags from the originating sales order to the generated delivery orders.
    *   Enables searching for delivery orders based on these synchronized tags.
    *   Offers optional visibility of the tags field in the delivery order list view (configurable via settings). The tag field is visible in form view only if it contains values.

*   **Manufacturing Order Quantity Lock:**
    *   Prevents modifications to the quantity in manufacturing orders after they have been confirmed.

*   **Purchase Order Splitting:**
    *   Splits purchase orders created from procurement based on the product category.

*   **Automated Delivery Notification:**
    *   Sends an automated email to the salesperson responsible for the original sales order when the associated delivery order is marked as delivered.

*   **Unique Category Names:**
    *   Enforces unique names for product categories.

*   **Clipboard Copy Widget:**
    *   Adds a custom widget to char fields that allows users to copy the field's content to the clipboard with a single click.

*   **Default Search Filter Modification:**
    *   Replaces the default "My Quotations" filter with a "Sales Orders" filter that displays confirmed and done sales orders by default.

## Contact

Jasmin Hirani - jasminhirani15@gmail.com

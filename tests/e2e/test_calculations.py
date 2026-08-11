import pytest
from playwright.sync_api import Page, expect

def test_bread_operations(page: Page):
    page.goto("http://127.0.0.1:8000")

    # 1. ADD
    page.fill("#operand1", "10")
    page.select_option("#operation", "add")
    page.fill("#operand2", "15")
    page.click("#submit-btn")

    # 2. BROWSE & READ
    row = page.locator('tr:has-text("25")')
    expect(row).to_be_visible()

    # 3. EDIT
    page.click('tr:has-text("25") button:has-text("Edit")')
    page.fill("#operand2", "20")
    page.click("#submit-btn")
    expect(page.locator('tr:has-text("30")')).to_be_visible()

    # 4. DELETE
    page.click('tr:has-text("30") button:has-text("Delete")')
    expect(page.locator('tr:has-text("30")')).not_to_be_visible()

def test_division_by_zero(page: Page):
    page.goto("http://127.0.0.1:8000")

    page.fill("#operand1", "10")
    page.select_option("#operation", "divide")
    page.fill("#operand2", "0")
    page.click("#submit-btn")

    error_msg = page.locator("#error-msg")
    expect(error_msg).to_contain_text("Cannot divide by zero.")

import datetime

# === STEP 1: Initialize counter ===
counter = 0

# === STEP 2: Function to generate PO number ===
def generate_po():
    global counter
    counter += 1
    today = datetime.datetime.now().strftime('%Y%m%d')
    return f"PO{today}{counter:06d}"

# === STEP 3: Main function to generate and enter PO ===
def enter_po():
    po_number = generate_po()
    Log.Message(f"Generated PO Number: {po_number}")

    # === STEP 4: Find your application's PO input field and enter the value ===
    # Example: Using NameMapping alias (you'll replace this with your actual object path)
    po_field = Aliases.browser.pageBearstoreTestsiteSmartbearCo.header.formSearch.textboxQ
    po_field.SetText(po_number)

    Log.Message(f"PO number {po_number} entered into the field successfully.")

# === STEP 5: Run it! ===
enter_po()
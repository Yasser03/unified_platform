import streamlit as st

def main():
    """Streamlit application for providing login links."""

    st.title("Web-Based Unified Login Platform")
    st.subheader("Please select your desired login destination:")

    # Use buttons for selection (more secure than dropdown)
    selected_website = None
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("S4Hana"):
            open_url_in_browser("https://ceaddev.adsc.ae/sap/bc/ui2/flp?sap-client=110&sap-language=EN#Shell-home")
    with col2:
        if st.button("SuccessFactors EC"):
            open_url_in_browser("https://hcm22preview.sapsf.com/sf/admin?bplte_company=abudhabispT1")
    with col3:
        if st.button("Payroll - EC"):
            open_url_in_browser("https://my040010.payroll.ondemand.com/sap/bc/gui/sap/its/webgui?sap-client=100&sap-language=EN#...")

    # Removed the if block for selected_website as we don't need to display links anymore
    st.write("If you require further assistance, please contact the COE administrator.")

def open_url_in_browser(url):
    """Opens the specified URL in the default web browser."""
    import webbrowser
    webbrowser.open(url)

if __name__ == "__main__":
    main()

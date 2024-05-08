import streamlit as st

def main():
    """Streamlit application for providing login links."""

    st.title("Web-Based Unified Login Platform")
    st.subheader("Please select your desired login destination:")

    # Use link buttons for selection (open in new tab)
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.link_button("S4Hana", "https://ceaddev.adsc.ae/sap/bc/ui2/flp?sap-client=110&sap-language=EN#Shell-home"):
            pass
    with col2:
        if st.link_button("SuccessFactors EC", "https://hcm22preview.sapsf.com/sf/admin?bplte_company=abudhabispT1"):
            pass
    with col3:
        if st.link_button("Payroll - EC", "https://my040010.payroll.ondemand.com/sap/bc/gui/sap/its/webgui?sap-client=100&sap-language=EN#..."):
            pass

    st.write("If you require further assistance, please contact the COE administrator.")

if __name__ == "__main__":
    main()

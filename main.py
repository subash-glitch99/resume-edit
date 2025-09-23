import parser
import editor.word_file_editor
from editor.word_file_editor import Editor

### Mock Values ###
newer_general_details = {
    'fullname': 'NISHEDH ADHIKARI',
    'title': 'Power Platform Developer',
    'phone': '+1 (469) 902-7570',
    'email': 'nishedhadhikari830@gmail.com',
    'professional_summary': (
        "ITSutraTes2 and results-driven Power Platform Developer with 8+ years of experience "
        "delivering enterprise-grade business applications across Healthcare, Banking, Retail, "
        "and Automotive industries. This is a test flag. Expertise in Canvas & Model-Driven Apps, Power Automate (Cloud & Desktop), "
        "Power BI, and Dataverse, with deep knowledge of CI/CD, ALM, CoE governance, and accessibility compliance (WCAG/ADA). "
        "Skilled in integrating Dynamics 365 CE with Azure Functions, REST APIs, SAP PI/PO, CDS Views, OData, and BAPI modules. "
        "Adept at leading fusion development teams, translating business needs into scalable solutions, and driving automation-first digital transformation strategies."
    )
}
newer_experience_details = {
    'Senior Power Platform / Dynamics 365 CRM DeveloperQuantum HealthJuly 2022 – Present': (
        "• Developed multilingual patient and provider management apps (Canvas & Model-Driven), deployed across U.S. & APAC.\n"
        "• Built role-based Power BI dashboards aligned with Dataverse security roles for clinicians, case managers, and compliance teams.\n"
        "• Automated claims adjudication and eligibility validation using custom plugins, C#, and .NET Core.\n"
        "• Designed CI/CD pipelines in Azure DevOps with gated deployments, rollback support, and automated unit tests.\n"
        "• Integrated Dynamics 365 CE with Epic & SAP via SAP PI/PO, CDS Views, OData, and BAPI modules.\n"
        "• Developed custom PCF controls and interactive forms for intake, validation, and formatting.\n"
        "• Implemented Power Automate flows for IT provisioning, incident management, and SLA-driven processes.\n"
        "• Built Power Virtual Agents chatbots and Copilot Studio solutions for internal and patient self-service.\n"
        "• Led accessibility compliance (WCAG 2.1 / Section 508) and multilingual application initiatives.\n"
        "• Authored technical design specs, mentored offshore teams, and enforced solution versioning via Azure DevOps."
    ),
    'Senior Power Platform / Dynamics 365 CRM DeveloperServiceLink, Pittsburgh, PAMar 2021 – June 2022': (
        "• Delivered patient and provider management apps across U.S. & APAC using Canvas & Model-Driven Apps.\n"
        "• Built role-based dashboards and embedded KPIs in Dynamics 365 CE using Power BI and Dataverse security.\n"
        "• Implemented CI/CD pipelines, custom plugins, synchronous workflows, and Azure Functions for dynamic rule evaluation.\n"
        "• Integrated Dynamics 365 CE with SAP, Salesforce Health Cloud, REST APIs, and Microsoft Graph.\n"
        "• Developed Power Pages portals for provider and patient onboarding, integrated with Azure SQL and Dataverse.\n"
        "• Automated complex approval routing, BPA, and enterprise workforce provisioning using Power Automate and Canvas Apps.\n"
        "• Ensured compliance with HIPAA/HITECH, accessibility (WCAG/ADA), and financial/privacy regulations.\n"
        "• Mentored offshore teams and standardized development via reusable component libraries."
    ),
    'Senior Power Platform / Dynamics 365 CRM DeveloperFirst Data Corporation, Atlanta, GAFeb 2019 – Feb 2021': (
        "• Developed multilingual patient and provider apps with Canvas & Model-Driven Apps.\n"
        "• Built Power BI dashboards with role-based access and KPIs for clinicians and operations.\n"
        "• Implemented CI/CD pipelines, plugins, Azure Functions, and Power Automate flows for claims and financial processes.\n"
        "• Integrated Dynamics 365 CE with SAP, Salesforce Financial Services Cloud, REST APIs, and Azure services.\n"
        "• Developed Power Pages portals, PCF controls, and middleware for regulatory compliance (KYC/AML).\n"
        "• Automated onboarding, provisioning, and HR workflows using Canvas Apps, Power Automate Desktop, and Azure Functions.\n"
        "• Ensured accessibility (WCAG/ADA), security compliance, and solution versioning via Azure DevOps."
    ),
    'Senior Power Platform / Dynamics 365 CRM DeveloperCommunity Health Systems, Nashville, TNSep 2017 – Jan 2019': (
        "• Built multilingual patient/provider apps using Canvas & Model-Driven Apps.\n"
        "• Developed role-based dashboards and embedded KPIs in CE using Power BI and Dataverse.\n"
        "• Implemented CI/CD pipelines, Azure Functions, Power Automate flows, and custom plugins for healthcare workflows.\n"
        "• Integrated Dynamics 365 CE with Epic, SAP, REST APIs, and external systems.\n"
        "• Created Power Pages portals and custom PCF controls for patient onboarding and clinical operations.\n"
        "• Automated enterprise processes for compliance, IT provisioning, and operational reporting.\n"
        "• Led accessibility (WCAG 2.1 / ADA) and security compliance initiatives.\n"
        "• Authored technical documentation, mentored offshore teams, and standardized solutions across teams."
    )
}

if __name__ == "__main__":

    test_file = "./test.docx"
    parsed_details = parser.parse_resume("./test.docx")

    editor =  Editor(parsed_details)

    editor.replace_professional_summary(parsed_details)

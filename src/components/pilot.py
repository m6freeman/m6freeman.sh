from rich.text import Text
from rich.padding import Padding
from rich.console import Group
from rich.markdown import Markdown


def build() -> Group:

    dotnet_engineer_2: Markdown = Markdown("""
**.NET Development Engineer II**

- Designs, develops, deploys, and continuously integrates `Dotnet` and `Python` serverless solutions, as well as containerized solutions alongside `Docker`, `ECR`, and `ECS`, with `Terraform` provisioned by `Github Action`
- Financial Transformation Project
    - Designed a prototype financial system integration and reporting solution and performed a demonstration of capabilities to executive leadership, ultimately resulting in the decision to not out-source the project
    - Performed requirements gathering and discovery for existing financial integrations for legacy system
    - Built an event-driven data processing pipeline using `AWS Lambda`, `S3`, `SQS`, and `DynamoDb` to perform ETL on millions of financial records a month, spanning 30+ systems with numerous document formats
    - Directly supported integration testing efforts alongside consultants and business partners
    - Provided business and diagnostic related data to a web front-end used by various levels of support as well as the business for reporting and to understand real-time metrics for financial records as they are submitted
    - Assisted in hyper-care efforts after initial go-live, directly assisting Accounts Payable, Accounts Recievable, and Corporate Accounting personnel troubleshoot system automation and data integration related tickets

    """)

    dotnet_engineer_1: Markdown = Markdown("""
**.NET Development Engineer I**

- Lead Engineer for Enterprise Document Archive System Upgrade Mobius 4 to 11
    - Modernized the legacy HR and Financial document archive system
        - Installed new version of software across distributed network of `AWS EC2` servers
        - Worked directly with database and cloud administrators to migrate existing data and schemas from on-prem to cloud
        - Performed requirements gathering and discovery for existing document ingestion pipeline
        - Updated, refactored, or entirely rewrote (when necessary) approx. 40 distributed `VB.NET` applications facilitating the traffic of documents into the archive across numerous on-prem and remote networks
    - Performed virtual and in-person training for dozens of employees with varying technical abilities, spanning 4 enterprise verticals, on the use of the product
    - Worked directly with the vendor on technical issues, troubleshooting outages, and performing minor version upgrades
    - Actively perform technical and administrative support
- Introduce new and modify existing features, perform debugging and patching, and perform project and infrastructural upgrades to legacy enterprise Financial, Payroll, HR, and Benefits solutions with `dotnet framework 4.x` to `dotnet8`, `Powershell`, and `VB.NET`
- Maintain and distribute `REST API`s, and customer facing web interfaces with `ASP.NET MVC`
    """)

    return Group(
        Padding(Text.assemble(
            ("Pilot Company, Knoxville TN ", "bold"),
            ("2021-present", "blockquote")), (0, 0, 0, 0)),
        Padding(dotnet_engineer_2, (1, 0, 0, 2)),
        Padding(dotnet_engineer_1, (1, 0, 0, 2)),
    )

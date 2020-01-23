## catalog

> OSCAL Control Catalog Format: JSON Schema

- Parameter: Parameters provide a mechanism for the dynamic assignment of value(s) in a control.
- Parameter label: A placeholder for a missing value, in display.
- Parameter description: Indicates and explains the purpose and use of a parameter
- Constraint: A formal or informal expression of a constraint or test
- Guideline: A prose statement that provides a recommendation for the use of a parameter.
- Value constraint: Indicates a permissible value for a parameter or property
- Selection: Presenting a choice among alternatives
- Choice: A value selection among several such options
- Part: A partition or component of a control or part
- Prose: Prose permits multiple paragraphs, lists, tables etc.
- Publication metadata: Provides information about the publication and availability of the containing document.
- Back matter: A collection of citations and resource references.
- Link: A reference to a local or remote resource
- Publication Timestamp: The date and time this document was published.
- Last modified timestamp: Date and time of last modification.
- Document version: The version of the document content.
- OSCAL version: OSCAL model version.
- Document Identifier: A document identifier qualified by an identifier type.
- Property: A value with a name, attributed to the containing control, part, or group.
- Annotation: A name/value pair with optional explanatory remarks.
- Party (organization or person): A responsible entity, either singular (an organization or person) or collective (multiple persons)
- Party Reference: References a party defined in metadata.
- Person: A person, with contact information
- Organization: An organization or legal entity (not a person), with contact information
- Personal Identifier: An identifier for a person (such as an ORCID) using a designated scheme.
- Organization Identifier: An identifier for an organization using a designated scheme.
- Resource link: A pointer to an external copy of a document with optional hash for verification
- Person Name: Full (legal) name of an individual
- Organization Name: Full (legal) name of an organization
- short-name: A common name, short name or acronym
- Address: A postal address.
- Address line: A single line of an address.
- City: City, town or geographical region for mailing address
- State: State, province or analogous geographical region for mailing address
- Postal Code: Postal or ZIP code for mailing address
- Country: Country for mailing address
- Email: Email address
- Telephone: Contact number by telephone
- URL: URL for web site or Internet presence
- Description: A short textual description
- Resource: A resource associated with the present document.
- Hash: A representation of a cryptographic digest generated over a resource using a hash algorithm.
- Role: Defining a role to be assigned to a party
- Responsible Party: A reference to a set of organizations or persons that have responsibility for performing a referenced role relative to the parent context.
- Title: A title for display and navigation
- Base64: 
- Citation: A citation to resources, either external or internal (by means of internal cross-reference).
- Citation target: An address for retrieval of a citation
- Remarks: Additional commentary on the parent item.
- Catalog: A collection of controls.
- Control Group: A group of controls, or of groups of controls.
- Control: A structured information object representing a security or privacy control. Each security or privacy control within the Catalog is defined by a distinct control instance.

## profile

> OSCAL Profile Metaschema: JSON Schema

- Publication metadata: Provides information about the publication and availability of the containing document.
- Back matter: A collection of citations and resource references.
- Link: A reference to a local or remote resource
- Publication Timestamp: The date and time this document was published.
- Last modified timestamp: Date and time of last modification.
- Document version: The version of the document content.
- OSCAL version: OSCAL model version.
- Document Identifier: A document identifier qualified by an identifier type.
- Property: A value with a name, attributed to the containing control, part, or group.
- Annotation: A name/value pair with optional explanatory remarks.
- Party (organization or person): A responsible entity, either singular (an organization or person) or collective (multiple persons)
- Party Reference: References a party defined in metadata.
- Person: A person, with contact information
- Organization: An organization or legal entity (not a person), with contact information
- Personal Identifier: An identifier for a person (such as an ORCID) using a designated scheme.
- Organization Identifier: An identifier for an organization using a designated scheme.
- Resource link: A pointer to an external copy of a document with optional hash for verification
- Person Name: Full (legal) name of an individual
- Organization Name: Full (legal) name of an organization
- short-name: A common name, short name or acronym
- Address: A postal address.
- Address line: A single line of an address.
- City: City, town or geographical region for mailing address
- State: State, province or analogous geographical region for mailing address
- Postal Code: Postal or ZIP code for mailing address
- Country: Country for mailing address
- Email: Email address
- Telephone: Contact number by telephone
- URL: URL for web site or Internet presence
- Description: A short textual description
- Resource: A resource associated with the present document.
- Hash: A representation of a cryptographic digest generated over a resource using a hash algorithm.
- Role: Defining a role to be assigned to a party
- Responsible Party: A reference to a set of organizations or persons that have responsibility for performing a referenced role relative to the parent context.
- Title: A title for display and navigation
- Base64: 
- Citation: A citation to resources, either external or internal (by means of internal cross-reference).
- Citation target: An address for retrieval of a citation
- Remarks: Additional commentary on the parent item.
- Parameter: Parameters provide a mechanism for the dynamic assignment of value(s) in a control.
- Parameter label: A placeholder for a missing value, in display.
- Parameter description: Indicates and explains the purpose and use of a parameter
- Constraint: A formal or informal expression of a constraint or test
- Guideline: A prose statement that provides a recommendation for the use of a parameter.
- Value constraint: Indicates a permissible value for a parameter or property
- Selection: Presenting a choice among alternatives
- Choice: A value selection among several such options
- Part: A partition or component of a control or part
- Prose: Prose permits multiple paragraphs, lists, tables etc.
- Profile: Each OSCAL profile is defined by a Profile element
- Import resource: An Import element designates a catalog, profile, or other resource to be included (referenced and potentially modified) by this profile.
- Merge controls: A Merge element merges controls in resolution.
- Combination rule: A Combine element defines whether and how to combine multiple (competing) versions of the same control
- As is: An As-is element indicates that the controls should be structured in resolution as they are structured in their source catalogs. It does not contain any elements or attributes.
- Custom grouping: A Custom element frames a structure for embedding represented controls in resolution.
- Control group: As in catalogs, a group of (selected) controls or of groups of controls
- Modify controls: Set parameters or amend controls in resolution
- Include controls: Specifies which controls to include from the resource (source catalog) being imported
- Include all: Include all controls from the imported resource (catalog)
- Call: Call a control by its ID
- Match controls by identifier: Select controls by (regular expression) match on ID
- Exclude controls: Which controls to exclude from the resource (source catalog) being imported
- Parameter Setting: A parameter setting, to be propagated to points of insertion
- Alteration: An Alter element specifies changes to be made to an included control when a profile is resolved.
- Removal: Specifies elements to be removed from a control, in resolution
- Addition: Specifies contents to be added into controls, in resolution

## component

> OSCAL Implementation Component Format: JSON Schema

- Publication metadata: Provides information about the publication and availability of the containing document.
- Back matter: A collection of citations and resource references.
- Link: A reference to a local or remote resource
- Publication Timestamp: The date and time this document was published.
- Last modified timestamp: Date and time of last modification.
- Document version: The version of the document content.
- OSCAL version: OSCAL model version.
- Document Identifier: A document identifier qualified by an identifier type.
- Property: A value with a name, attributed to the containing control, part, or group.
- Annotation: A name/value pair with optional explanatory remarks.
- Party (organization or person): A responsible entity, either singular (an organization or person) or collective (multiple persons)
- Party Reference: References a party defined in metadata.
- Person: A person, with contact information
- Organization: An organization or legal entity (not a person), with contact information
- Personal Identifier: An identifier for a person (such as an ORCID) using a designated scheme.
- Organization Identifier: An identifier for an organization using a designated scheme.
- Resource link: A pointer to an external copy of a document with optional hash for verification
- Person Name: Full (legal) name of an individual
- Organization Name: Full (legal) name of an organization
- short-name: A common name, short name or acronym
- Address: A postal address.
- Address line: A single line of an address.
- City: City, town or geographical region for mailing address
- State: State, province or analogous geographical region for mailing address
- Postal Code: Postal or ZIP code for mailing address
- Country: Country for mailing address
- Email: Email address
- Telephone: Contact number by telephone
- URL: URL for web site or Internet presence
- Description: A short textual description
- Resource: A resource associated with the present document.
- Hash: A representation of a cryptographic digest generated over a resource using a hash algorithm.
- Role: Defining a role to be assigned to a party
- Responsible Party: A reference to a set of organizations or persons that have responsibility for performing a referenced role relative to the parent context.
- Title: A title for display and navigation
- Base64: 
- Citation: A citation to resources, either external or internal (by means of internal cross-reference).
- Citation target: An address for retrieval of a citation
- Description: A description supporting the parent item.
- Remarks: Additional commentary on the parent item.
- Specific Statement: Describes which specific statements are addressed by a requirement, by pointing to a specific requirement statement within a control.
- Incorporates Component: TBD
- Incorporates Capability: TBD
- Component Definition: TBD
- Import Component Definition: Loads a component definition from another resource.
- Component: A defined component that can be part of an implemented system.
- Capability: A grouping of other components and/or capabilities.
- Control Implementation: Defines how the component or capability supports a set of controls.
- Can Meet: Defines what sets of controls are supported by the component.
- Control-based Requirement: TBD

## ssp

> OSCAL System Security Plan (SSP) Format: JSON Schema

- Publication metadata: Provides information about the publication and availability of the containing document.
- Back matter: A collection of citations and resource references.
- Link: A reference to a local or remote resource
- Publication Timestamp: The date and time this document was published.
- Last modified timestamp: Date and time of last modification.
- Document version: The version of the document content.
- OSCAL version: OSCAL model version.
- Document Identifier: A document identifier qualified by an identifier type.
- Property: A value with a name, attributed to the containing control, part, or group.
- Annotation: A name/value pair with optional explanatory remarks.
- Party (organization or person): A responsible entity, either singular (an organization or person) or collective (multiple persons)
- Party Reference: References a party defined in metadata.
- Person: A person, with contact information
- Organization: An organization or legal entity (not a person), with contact information
- Personal Identifier: An identifier for a person (such as an ORCID) using a designated scheme.
- Organization Identifier: An identifier for an organization using a designated scheme.
- Resource link: A pointer to an external copy of a document with optional hash for verification
- Person Name: Full (legal) name of an individual
- Organization Name: Full (legal) name of an organization
- short-name: A common name, short name or acronym
- Address: A postal address.
- Address line: A single line of an address.
- City: City, town or geographical region for mailing address
- State: State, province or analogous geographical region for mailing address
- Postal Code: Postal or ZIP code for mailing address
- Country: Country for mailing address
- Email: Email address
- Telephone: Contact number by telephone
- URL: URL for web site or Internet presence
- Description: A short textual description
- Resource: A resource associated with the present document.
- Hash: A representation of a cryptographic digest generated over a resource using a hash algorithm.
- Role: Defining a role to be assigned to a party
- Responsible Party: A reference to a set of organizations or persons that have responsibility for performing a referenced role relative to the parent context.
- Title: A title for display and navigation
- Base64: 
- Citation: A citation to resources, either external or internal (by means of internal cross-reference).
- Citation target: An address for retrieval of a citation
- Description: A description supporting the parent item.
- Remarks: Additional commentary on the parent item.
- System Security Plan (SSP): A system security plan, such as those described in NIST SP 800-18
- Import Profile: Used to import the OSCAL profile representing the system's control baseline.
- System Characteristics: Contains the characteristics of the system, such as its name, purpose, and security impact level.
- System Identification: A unique identifier for the system described by this system security plan.
- System Name (Full): The full name of the system.
- System Name (Short): A short name for the system, such as an acronym, that is suitable for display in a data table or summary list.
- Security Sensitivity Level: The overall information system sensitivity categorization, such as defined by FIPS-199.
- System Information: Contains details about all information types that are stored, processed, or transmitted by the system, such as privacy information, and those defined in NIST SP 800-60.
- Information Type: Contains details about one information type that is stored, processed, or transmitted by the system, such as privacy information, and those defined in NIST SP 800-60.
- Information Type Identifier: An identifier qualified by the given identification system used, such as NIST SP 800-60.
- Confidentiality Impact Level: The expected level of impact resulting from the unauthorized disclosure of information.
- Integrity Impact Level: The expected level of impact resulting from the unauthorized modification of information.
- Availability Impact Level: The expected level of impact resulting from the disruption of access to or use of information or the information system.
- Base Level (Confidentiality, Integrity, or Availability): The prescribed base (Confidentiality, Integrity, or Availability) security impact level.
- Selected Level (Confidentiality, Integrity, or Availability): The selected (Confidentiality, Integrity, or Availability) security impact level.
- Adjustment Justification: If the selected security level is different from the base security level, this contains the justification for the change.
- Security Impact Level: The overall level of expected impact resulting from unauthorized disclosure, modification, or loss of access to information.
- Security Objective: Confidentiality: A target-level of confidentiality for the system, based on the sensitivity of information within the system.
- Security Objective: Integrity: A target-level of integrity for the system, based on the sensitivity of information within the system.
- Security Objective: Availability: A target-level of availability for the system, based on the sensitivity of information within the system.
- Status: Describes the operational status of the system.
- Leveraged Authorization: A description of another authorized system from which this system inherits capabilities that satisfy security requirements. Another term for this concept is a common control provider.
- System Authorization Date: The date this system received its authorization.
- Authorization Boundary: A description of this system's authorization boundary, optionally supplemented by diagrams that illustrate the authorization boundary.
- Diagram: A graphic that provides a visual representation the system, or some aspect of it.
- Caption: A brief caption to annotate the diagram.
- Network Architecture: A description of the system's network architecture, optionally supplemented by diagrams that illustrate the network architecture.
- Data Flow: A description of the logical flow of information within the system and across its boundaries, optionally supplemented by diagrams that illustrate these flows.
- System Implementation: Provides information as to how the system is implemented.
- System User Class: A type of user that interacts with the system based on an associated role.
- Role Identifier Reference: A reference to the roles served by the user.
- Privilege: Identifies a specific system privilege held by the user, along with an associated description and/or rationale for the privilege.
- Functions Performed: Describes a function performed for a given authorized privilege by this user class.
- Component: A defined component that can be part of an implemented system.
- Service: Information about an individual service within the system.
- Protocol: Information about the protocol used to provide a service.
- Port Range: Where applicable this is the IPv4 port range on which the service operates.
- Purpose: Describes the purpose for the service within the system.
- Interconnection: Details on an individual system interconnection.
- Remote Interconnected System Name: The name of the remote interconnected system.
- System Inventory: A set of inventory-item entries that represent the managed inventory instances of the system.
- Inventory Item: A single managed inventory item within the system.
- Implemented Component: The set of componenets that are implemented in a given system inventory item.
- Control Implementation: Describes how the system satisfies a set of controls.
- Control-based Requirement: Describes how the system satisfies an individual control.
- Specific Statement: Identifies which statements within a control are addressed.
- Responsible Role: A reference to one or more roles with responsibility for performing a function relative to the control.
- Component Control Implementation: Defines how the referenced component implements a set of controls.
- Set Parameter Value: Identifies the parameter that will be filled in by the enclosed value element.
- Value: The phrase or string that fills-in the parameter and completes the requirement statement.

<a id='activity-uuid'/>
- **Activity ID**(`activity-uuid` `type:string`) is found in [assessment-plan](assessment-plan.html), [assessment-results](assessment-results.html) & [poam](poam.html)
  - definition: Links the task to a defined activity.
<a id='add'/>
- **Addition**(`add` `type:object`) is found in [profile](profile.html)
  - definition: Specifies contents to be added into controls, in resolution
<a id='addr-line'/>
- **Address line**(`addr-line` `type:string`) is found in [assessment-plan](assessment-plan.html), [assessment-results](assessment-results.html), [catalog](catalog.html), [component](component.html), [poam](poam.html), [profile](profile.html) & [ssp](ssp.html)
  - definition: A single line of an address.
<a id='address'/>
- **Address**(`address` `type:object`) is found in [assessment-plan](assessment-plan.html), [assessment-results](assessment-results.html), [catalog](catalog.html), [component](component.html), [poam](poam.html), [profile](profile.html) & [ssp](ssp.html)
  - definition: A postal address.
<a id='adjustment-justification'/>
- **Adjustment Justification**(`adjustment-justification` `type:string`) is found in [ssp](ssp.html)
  - definition: If the selected security level is different from the base security level, this contains the justification for the change.
<a id='all'/>
- **Include all**(`all` `type:object`) is found in [assessment-plan](assessment-plan.html), [assessment-results](assessment-results.html) & [profile](profile.html)
  - definition for **Include all** is different between these schemas
    - assessment-plan: A key word to indicate all
    - assessment-results: A key word to indicate all
    - profile: Include all controls from the imported resource (catalog)
<a id='alter'/>
- **Alteration**(`alter` `type:object`) is found in [profile](profile.html)
  - definition: An Alter element specifies changes to be made to an included control when a profile is resolved.
<a id='annotation'/>
- **Annotation**(`annotation` `type:object`) is found in [assessment-plan](assessment-plan.html), [assessment-results](assessment-results.html), [catalog](catalog.html), [component](component.html), [poam](poam.html), [profile](profile.html) & [ssp](ssp.html)
  - definition: A name/value pair with optional explanatory remarks.
<a id='as-is'/>
- **As is**(`as-is` `type:boolean`) is found in [profile](profile.html)
  - definition: An As-is element indicates that the controls should be structured in resolution as they are structured in their source catalogs. It does not contain any elements or attributes.
<a id='assessment-activities'/>
- **Assessment Activities**(`assessment-activities` `type:object`) is found in [assessment-plan](assessment-plan.html) & [assessment-results](assessment-results.html)
  - definition: Identifies the assessment activities and schedule. In the assessment plan, these are planned activities. In the assessment results, these are the actual activities performed.
<a id='assessment-method'/>
- **Assessment Method**(`assessment-method` `type:object`) is found in [assessment-plan](assessment-plan.html) & [assessment-results](assessment-results.html)
  - definition: Identifies a method for assessing the satisfaction of this objective.
<a id='assessment-plan'/>
- **Security Assessment Plan (SAP)**(`assessment-plan` `type:object`) is found in [assessment-plan](assessment-plan.html)
  - definition: An assessment plan, such as those provided by a FedRAMP assessor.
<a id='assessment-results'/>
- **Security Assessment Results (SAR)**(`assessment-results` `type:object`) is found in [assessment-results](assessment-results.html)
  - definition: Security assessment results, such as those provided by a FedRAMP assessor in the FedRAMP Security Assessment Report.
<a id='assessment-subjects'/>
- **Subject of Assessment**(`assessment-subjects` `type:object`) is found in [assessment-plan](assessment-plan.html) & [assessment-results](assessment-results.html)
  - definition: Identifies system elements being assessed, such as components, inventory items, and locations. In the assessment plan, this identifies the planned assessment subject. In the assessment results this is the actual assessment subject, and reflects any changes from the plan.
<a id='assessor'/>
- **Assessor**(`assessor` `type:object`) is found in [assessment-results](assessment-results.html) & [poam](poam.html)
  - definition: Identifies an individual who gathered the evidence resulting in the observation or risk identification.
<a id='assets'/>
- **Assessment Assets**(`assets` `type:object`) is found in [assessment-plan](assessment-plan.html) & [assessment-results](assessment-results.html)
  - definition: Identifies the assets used to perform this assessment, such as the assessment team, scanning tools, and assumptions.
<a id='authorization-boundary'/>
- **Authorization Boundary**(`authorization-boundary` `type:object`) is found in [ssp](ssp.html)
  - definition: A description of this system's authorization boundary, optionally supplemented by diagrams that illustrate the authorization boundary.
<a id='authorized-privilege'/>
- **Privilege**(`authorized-privilege` `type:object`) is found in [assessment-plan](assessment-plan.html), [assessment-results](assessment-results.html) & [ssp](ssp.html)
  - definition: Identifies a specific system privilege held by the user, along with an associated description and/or rationale for the privilege.
<a id='availability-impact'/>
- **Availability Impact Level**(`availability-impact` `type:object`) is found in [ssp](ssp.html)
  - definition: The expected level of impact resulting from the disruption of access to or use of information or the information system.
<a id='back-matter'/>
- **Back matter**(`back-matter` `type:object`) is found in [assessment-plan](assessment-plan.html), [assessment-results](assessment-results.html), [catalog](catalog.html), [component](component.html), [poam](poam.html), [profile](profile.html) & [ssp](ssp.html)
  - definition: A collection of citations and resource references.
<a id='base'/>
- **Base Level (Confidentiality, Integrity, or Availability)**(`base` `type:string`) is found in [ssp](ssp.html)
  - definition: The prescribed base (Confidentiality, Integrity, or Availability) security impact level.
<a id='base64'/>
- **Base64**(`base64` `type:object`) is found in [assessment-plan](assessment-plan.html), [assessment-results](assessment-results.html), [catalog](catalog.html), [component](component.html), [poam](poam.html), [profile](profile.html) & [ssp](ssp.html)
  - definition: 
<a id='biblio'/>
- **Bibliographic Definition**(`biblio` `type:object`) is found in [assessment-plan](assessment-plan.html), [assessment-results](assessment-results.html), [catalog](catalog.html), [component](component.html), [poam](poam.html), [profile](profile.html) & [ssp](ssp.html)
  - definition: A container in which a set of bibliographic information can included. The model of this information is undefined by OSCAL.
<a id='by-component'/>
- **Component Control Implementation**(`by-component` `type:object`) is found in [ssp](ssp.html)
  - definition: Defines how the referenced component implements a set of controls.
<a id='call'/>
- **Call**(`call` `type:object`) is found in [profile](profile.html)
  - definition: Call a control by its ID
<a id='capability'/>
- **Capability**(`capability` `type:object`) is found in [component](component.html)
  - definition: A grouping of other components and/or capabilities.
<a id='caption'/>
- **Caption**(`caption` `type:string`) is found in [ssp](ssp.html)
  - definition: A brief caption to annotate the diagram.
<a id='catalog'/>
- **Catalog**(`catalog` `type:object`) is found in [catalog](catalog.html)
  - definition: A collection of controls.
<a id='choice'/>
- **Choice**(`choice` `type:string`) is found in [catalog](catalog.html) & [profile](profile.html)
  - definition: A value selection among several such options
<a id='citation'/>
- **Citation**(`citation` `type:object`) is found in [assessment-plan](assessment-plan.html), [assessment-results](assessment-results.html), [catalog](catalog.html), [component](component.html), [poam](poam.html), [profile](profile.html) & [ssp](ssp.html)
  - definition: A citation consisting of end note text and optional structured bibliographic data.
<a id='city'/>
- **City**(`city` `type:string`) is found in [assessment-plan](assessment-plan.html), [assessment-results](assessment-results.html), [catalog](catalog.html), [component](component.html), [poam](poam.html), [profile](profile.html) & [ssp](ssp.html)
  - definition: City, town or geographical region for mailing address
<a id='closure-actions'/>
- **Closer Actions**(`closure-actions` `type:string`) is found in [assessment-results](assessment-results.html) & [poam](poam.html)
  - definition: Describes the actions taken that resulted in the closure of the identified risk.
<a id='combine'/>
- **Combination rule**(`combine` `type:object`) is found in [profile](profile.html)
  - definition: A Combine element defines whether and how to combine multiple (competing) versions of the same control
<a id='compare-to'/>
- **Compare To**(`compare-to` `type:string`) is found in [assessment-plan](assessment-plan.html), [assessment-results](assessment-results.html) & [poam](poam.html)
  - definition: Typically used in when copying content from the assessment plan to the assessment results. The uuid should be changed in the assessment results file, and the compare-to field should be set to the original assessment plan uuid value. This enables the plan and results to be compared later to identify what changed between the two.
<a id='component'/>
- **Component**(`component` `type:object`) is found in [assessment-plan](assessment-plan.html), [assessment-results](assessment-results.html), [component](component.html), [poam](poam.html) & [ssp](ssp.html)
  - definition for **Component** is different between these schemas
    - assessment-plan: A defined component that can be part of an implemented system.
    - assessment-results: A defined component that can be part of an implemented system.
    - component: A defined component that can be part of an implemented system.
    - poam: A defined component that can be part of an implemented system.
    - ssp: A defined component that can be part of an implemented system.
<a id='component-definition'/>
- **Component Definition**(`component-definition` `type:object`) is found in [component](component.html)
  - definition: A collection of component descriptions, which may optionally be grouped by capability.
<a id='confidentiality-impact'/>
- **Confidentiality Impact Level**(`confidentiality-impact` `type:object`) is found in [ssp](ssp.html)
  - definition: The expected level of impact resulting from the unauthorized disclosure of information.
<a id='constraint'/>
- **Constraint**(`constraint` `type:object`) is found in [catalog](catalog.html) & [profile](profile.html)
  - definition: A formal or informal expression of a constraint or test
<a id='control'/>
- **Control**(`control` `type:object`) is found in [catalog](catalog.html)
  - definition: A structured information object representing a security or privacy control. Each security or privacy control within the Catalog is defined by a distinct control instance.
<a id='control-implementation'/>
- **Control Implementation**(`control-implementation` `type:object`) is found in [component](component.html) & [ssp](ssp.html)
  - definition for **Control Implementation** is different between these schemas
    - component: Defines how the component or capability supports a set of controls.
    - ssp: Describes how the system satisfies a set of controls.
<a id='control-objectives'/>
- **Control Objectives**(`control-objectives` `type:object`) is found in [assessment-plan](assessment-plan.html) & [assessment-results](assessment-results.html)
  - definition: Identifies the control objectives of the assessment. In the assessment plan, these are the planned objectives. In the assessment results, these are the actual objectives, and reflects any changes from the plan.
<a id='controls'/>
- **Assessed Controls**(`controls` `type:object`) is found in [assessment-plan](assessment-plan.html) & [assessment-results](assessment-results.html)
  - definition: Identifies the controls being assessed. In the assessment plan, these are the planned controls. In the assessment results, these are the actual controls, and reflects any changes from the plan.
<a id='country'/>
- **Country**(`country` `type:string`) is found in [assessment-plan](assessment-plan.html), [assessment-results](assessment-results.html), [catalog](catalog.html), [component](component.html), [poam](poam.html), [profile](profile.html) & [ssp](ssp.html)
  - definition: Country for mailing address
<a id='custom'/>
- **Custom grouping**(`custom` `type:object`) is found in [profile](profile.html)
  - definition: A Custom element frames a structure for embedding represented controls in resolution.
<a id='data-flow'/>
- **Data Flow**(`data-flow` `type:object`) is found in [ssp](ssp.html)
  - definition: A description of the logical flow of information within the system and across its boundaries, optionally supplemented by diagrams that illustrate these flows.
<a id='date-authorized'/>
- **System Authorization Date**(`date-authorized` `type:string`) is found in [ssp](ssp.html)
  - definition: The date this system received its authorization.
<a id='date-time-stamp'/>
- **Date/Time Stamp**(`date-time-stamp` `type:string`) is found in [assessment-results](assessment-results.html) & [poam](poam.html)
  - definition: Date/time stamp identifying when the information was collected.
<a id='desc'/>
- **Description**(`desc` `type:string`) is found in [assessment-plan](assessment-plan.html), [assessment-results](assessment-results.html), [catalog](catalog.html), [component](component.html), [poam](poam.html), [profile](profile.html) & [ssp](ssp.html)
  - definition: A short textual description
<a id='description'/>
- **Description**(`description` `type:string`) is found in [assessment-plan](assessment-plan.html), [assessment-results](assessment-results.html), [component](component.html), [poam](poam.html) & [ssp](ssp.html)
  - definition: A description supporting the parent item.
<a id='diagram'/>
- **Diagram**(`diagram` `type:object`) is found in [ssp](ssp.html)
  - definition: A graphic that provides a visual representation the system, or some aspect of it.
<a id='doc-id'/>
- **Document Identifier**(`doc-id` `type:object`) is found in [assessment-plan](assessment-plan.html), [assessment-results](assessment-results.html), [catalog](catalog.html), [component](component.html), [poam](poam.html), [profile](profile.html) & [ssp](ssp.html)
  - definition: A document identifier qualified by an identifier type.
<a id='email'/>
- **Email**(`email` `type:string`) is found in [assessment-plan](assessment-plan.html), [assessment-results](assessment-results.html), [catalog](catalog.html), [component](component.html), [poam](poam.html), [profile](profile.html) & [ssp](ssp.html)
  - definition: Email address
<a id='end'/>
- **End**(`end` `type:string`) is found in [assessment-plan](assessment-plan.html), [assessment-results](assessment-results.html) & [poam](poam.html)
  - definition: Identifies the end of a task.
<a id='exclude'/>
- **Exclude controls**(`exclude` `type:object`) is found in [profile](profile.html)
  - definition: Which controls to exclude from the resource (source catalog) being imported
<a id='exclude-activity'/>
- **Included Activity**(`exclude-activity` `type:object`) is found in [assessment-plan](assessment-plan.html) & [assessment-results](assessment-results.html)
  - definition: Identifies an activity explicitly excluded from the assessment. In the assessment plan, this clarifies activities that are out-of-scope or prohibited. In the assessment results, this could be used to explicitly identify an activity that was planned, but not performed.
<a id='exclude-control'/>
- **Exclude Control**(`exclude-control` `type:object`) is found in [assessment-plan](assessment-plan.html) & [assessment-results](assessment-results.html)
  - definition: Identifies an individual control to exclude.
<a id='exclude-objective'/>
- **Exclude Objective**(`exclude-objective` `type:object`) is found in [assessment-plan](assessment-plan.html) & [assessment-results](assessment-results.html)
  - definition: Identifies an individual control objective to exclude.
<a id='exclude-subject'/>
- **Excluded Assessment Subject**(`exclude-subject` `type:object`) is found in [assessment-plan](assessment-plan.html) & [assessment-results](assessment-results.html)
  - definition: Identifies what is explicitly excluded from this assessment. Used to remove a subset of items from groups of explicitly included items. Also used to explicitly clarify off-limit items, such as hosts to avoid scanning.
<a id='external-id'/>
- **Personal Identifier**(`external-id` `type:object`) is found in [assessment-plan](assessment-plan.html), [assessment-results](assessment-results.html), [catalog](catalog.html), [component](component.html), [poam](poam.html), [profile](profile.html) & [ssp](ssp.html)
  - definition: An identifier for a person (such as an ORCID) using a designated scheme.
<a id='finding'/>
- **Finding**(`finding` `type:object`) is found in [assessment-results](assessment-results.html) & [poam](poam.html)
  - definition: Describes an individual finding.
<a id='function-performed'/>
- **Functions Performed**(`function-performed` `type:string`) is found in [assessment-plan](assessment-plan.html), [assessment-results](assessment-results.html) & [ssp](ssp.html)
  - definition: Describes a function performed for a given authorized privilege by this user class.
<a id='group'/>
- **Control group**(`group` `type:object`) is found in [catalog](catalog.html) & [profile](profile.html)
  - definition for **Control group** is different between these schemas
    - catalog: A group of controls, or of groups of controls.
    - profile: As in catalogs, a group of (selected) controls or of groups of controls
<a id='guideline'/>
- **Guideline**(`guideline` `type:object`) is found in [catalog](catalog.html) & [profile](profile.html)
  - definition: A prose statement that provides a recommendation for the use of a parameter.
<a id='hash'/>
- **Hash**(`hash` `type:object`) is found in [assessment-plan](assessment-plan.html), [assessment-results](assessment-results.html), [catalog](catalog.html), [component](component.html), [poam](poam.html), [profile](profile.html) & [ssp](ssp.html)
  - definition: A representation of a cryptographic digest generated over a resource using a hash algorithm.
<a id='implementation-statement-uuid'/>
- **Implementation Statement UUID**(`implementation-statement-uuid` `type:string`) is found in [assessment-results](assessment-results.html) & [poam](poam.html)
  - definition: Identifies the implementation statement in the SSP to which this finding is related.
<a id='implementation-status'/>
- **Implementation Status**(`implementation-status` `type:object`) is found in [assessment-results](assessment-results.html) & [poam](poam.html)
  - definition: Identifies the implementation status of the control or control objective.
<a id='implemented-component'/>
- **Implemented Component**(`implemented-component` `type:object`) is found in [assessment-plan](assessment-plan.html), [assessment-results](assessment-results.html), [poam](poam.html) & [ssp](ssp.html)
  - definition: The set of componenets that are implemented in a given system inventory item.
<a id='implemented-requirement'/>
- **Control-based Requirement**(`implemented-requirement` `type:object`) is found in [component](component.html) & [ssp](ssp.html)
  - definition for **Control-based Requirement** is different between these schemas
    - component: Describes how the component implements an individual control.
    - ssp: Describes how the system satisfies an individual control.
<a id='import'/>
- **Import resource**(`import` `type:object`) is found in [profile](profile.html)
  - definition: An Import element designates a catalog, profile, or other resource to be included (referenced and potentially modified) by this profile.
<a id='import-ap'/>
- **Import Assessment Plan**(`import-ap` `type:object`) is found in [assessment-results](assessment-results.html)
  - definition: Used by assessment-results to import information about the original plan for assessing the system.
<a id='import-component-definition'/>
- **Import Component Definition**(`import-component-definition` `type:object`) is found in [component](component.html)
  - definition: Loads a component definition from another resource.
<a id='import-profile'/>
- **Import Profile**(`import-profile` `type:object`) is found in [ssp](ssp.html)
  - definition: Used to import the OSCAL profile representing the system's control baseline.
<a id='import-ssp'/>
- **Import System Security Plan**(`import-ssp` `type:object`) is found in [assessment-plan](assessment-plan.html) & [poam](poam.html)
  - definition: Used by the assessment plan and POA&M to import information about the system.
<a id='include'/>
- **Include controls**(`include` `type:object`) is found in [profile](profile.html)
  - definition: Specifies which controls to include from the resource (source catalog) being imported
<a id='include-activity'/>
- **Included Activity**(`include-activity` `type:object`) is found in [assessment-plan](assessment-plan.html) & [assessment-results](assessment-results.html)
  - definition: Identifies an assessment activity. In the assessment plan, this is an intended/in-scope activity. In the assessment results, this identifies an activity that was actually performed.
<a id='include-control'/>
- **Include Control**(`include-control` `type:object`) is found in [assessment-plan](assessment-plan.html) & [assessment-results](assessment-results.html)
  - definition: Identifies an individual control to include.
<a id='include-objective'/>
- **Include Objective**(`include-objective` `type:object`) is found in [assessment-plan](assessment-plan.html) & [assessment-results](assessment-results.html)
  - definition: Identifies an individual control objective to include.
<a id='include-subject'/>
- **Included Assessment Subject**(`include-subject` `type:object`) is found in [assessment-plan](assessment-plan.html) & [assessment-results](assessment-results.html)
  - definition: Identifies exactly what will be the focus of this assessment. Anything not explicitly defined is out-of-scope.
<a id='incorporates-component'/>
- **Incorporates Component**(`incorporates-component` `type:object`) is found in [component](component.html)
  - definition: TBD
<a id='information-type'/>
- **Information Type**(`information-type` `type:object`) is found in [ssp](ssp.html)
  - definition: Contains details about one information type that is stored, processed, or transmitted by the system, such as privacy information, and those defined in NIST SP 800-60.
<a id='information-type-id'/>
- **Information Type Identifier**(`information-type-id` `type:object`) is found in [ssp](ssp.html)
  - definition: An identifier qualified by the given identification system used, such as NIST SP 800-60.
<a id='integrity-impact'/>
- **Integrity Impact Level**(`integrity-impact` `type:object`) is found in [ssp](ssp.html)
  - definition: The expected level of impact resulting from the unauthorized modification of information.
<a id='inventory-item'/>
- **Inventory Item**(`inventory-item` `type:object`) is found in [assessment-plan](assessment-plan.html), [assessment-results](assessment-results.html), [poam](poam.html) & [ssp](ssp.html)
  - definition: A single managed inventory item within the system.
<a id='label'/>
- **Parameter label**(`label` `type:string`) is found in [catalog](catalog.html) & [profile](profile.html)
  - definition: A placeholder for a missing value, in display.
<a id='last-modified'/>
- **Last modified timestamp**(`last-modified` `type:string`) is found in [assessment-plan](assessment-plan.html), [assessment-results](assessment-results.html), [catalog](catalog.html), [component](component.html), [poam](poam.html), [profile](profile.html) & [ssp](ssp.html)
  - definition: Date and time of last modification.
<a id='leveraged-authorization'/>
- **Leveraged Authorization**(`leveraged-authorization` `type:object`) is found in [ssp](ssp.html)
  - definition: A description of another authorized system from which this system inherits capabilities that satisfy security requirements. Another term for this concept is a common control provider.
<a id='link'/>
- **Link**(`link` `type:object`) is found in [assessment-plan](assessment-plan.html), [assessment-results](assessment-results.html), [catalog](catalog.html), [component](component.html), [poam](poam.html), [profile](profile.html) & [ssp](ssp.html)
  - definition: A reference to a local or remote resource
<a id='local-definitions'/>
- **Local Definitions**(`local-definitions` `type:object`) is found in [assessment-plan](assessment-plan.html), [assessment-results](assessment-results.html) & [poam](poam.html)
  - definition for **Local Definitions** is different between these schemas
    - assessment-plan: Allows control objectives, users, components, and inventory-items to be defined within the assessment plan or assessment results for circumstances where they are not appropriately defined in the SSP. NOTE: Use the assessment plan or assessment results metadata to define additional locations if needed.
    - assessment-results: Allows control objectives, users, components, and inventory-items to be defined within the assessment plan or assessment results for circumstances where they are not appropriately defined in the SSP. NOTE: Use the assessment plan or assessment results metadata to define additional locations if needed.
    - poam: Allows components, and inventory-items to be defined within the POA&M for circumstances where no OSCAL-based SSP exists, or is not delivered with the POA&M.
<a id='location'/>
- **Location**(`location` `type:object`) is found in [assessment-plan](assessment-plan.html), [assessment-results](assessment-results.html), [catalog](catalog.html), [component](component.html), [poam](poam.html), [profile](profile.html) & [ssp](ssp.html)
  - definition: A location, with associated metadata that can be referenced.
<a id='location-uuid'/>
- **Location Reference**(`location-uuid` `type:string`) is found in [assessment-plan](assessment-plan.html), [assessment-results](assessment-results.html), [catalog](catalog.html), [component](component.html), [poam](poam.html), [profile](profile.html) & [ssp](ssp.html)
  - definition: References a location defined in metadata.
<a id='match'/>
- **Match controls by identifier**(`match` `type:object`) is found in [profile](profile.html)
  - definition: Select controls by (regular expression) match on ID
<a id='member-of-organization'/>
- **Organizational Affiliation**(`member-of-organization` `type:string`) is found in [assessment-plan](assessment-plan.html), [assessment-results](assessment-results.html), [catalog](catalog.html), [component](component.html), [poam](poam.html), [profile](profile.html) & [ssp](ssp.html)
  - definition: Identifies that the containing object is a member of the organization associated with the provided UUID.
<a id='merge'/>
- **Merge controls**(`merge` `type:object`) is found in [profile](profile.html)
  - definition: A Merge element merges controls in resolution.
<a id='metadata'/>
- **Publication metadata**(`metadata` `type:object`) is found in [assessment-plan](assessment-plan.html), [assessment-results](assessment-results.html), [catalog](catalog.html), [component](component.html), [poam](poam.html), [profile](profile.html) & [ssp](ssp.html)
  - definition: Provides information about the publication and availability of the containing document.
<a id='method'/>
- **Assessment Method**(`method` `type:object`) is found in [assessment-plan](assessment-plan.html) & [assessment-results](assessment-results.html)
  - definition: A local definition of a control objective. Uses catalog syntax for control objective and assessment actions.
<a id='mitigating-factor'/>
- **Mitigating Factor**(`mitigating-factor` `type:object`) is found in [assessment-results](assessment-results.html) & [poam](poam.html)
  - definition: Describes a mitigating factor with an optional link to an implementation statement in the SSP.
<a id='modify'/>
- **Modify controls**(`modify` `type:object`) is found in [profile](profile.html)
  - definition: Set parameters or amend controls in resolution
<a id='network-architecture'/>
- **Network Architecture**(`network-architecture` `type:object`) is found in [ssp](ssp.html)
  - definition: A description of the system's network architecture, optionally supplemented by diagrams that illustrate the network architecture.
<a id='objective'/>
- **Control Objective**(`objective` `type:object`) is found in [assessment-plan](assessment-plan.html) & [assessment-results](assessment-results.html)
  - definition: A local definition of a control objective. Uses catalog syntax for control objective and assessment actions.
<a id='objective-status'/>
- **Implementation Status**(`objective-status` `type:object`) is found in [assessment-results](assessment-results.html) & [poam](poam.html)
  - definition: Captures an assessors conclusions as to whether an objective is fully satisfied.
<a id='objectives'/>
- **Objectives of Assessment**(`objectives` `type:object`) is found in [assessment-plan](assessment-plan.html) & [assessment-results](assessment-results.html)
  - definition: Identifies the controls and control being assessed and their control objectives. In the assessment plans, these are the planned controls and objectives. In the assessment results, these are the actual controls and objectives, and reflects any changes from the plan.
<a id='observation'/>
- **Objective**(`observation` `type:object`) is found in [assessment-results](assessment-results.html) & [poam](poam.html)
  - definition: Describes an individual observation.
<a id='observation-method'/>
- **Observation Method**(`observation-method` `type:string`) is found in [assessment-results](assessment-results.html) & [poam](poam.html)
  - definition: Identifies how the observation was made.
<a id='observation-type'/>
- **Observation Type**(`observation-type` `type:string`) is found in [assessment-results](assessment-results.html) & [poam](poam.html)
  - definition: Identifies the nature of the observation. More than one may be used to further qualify and enable filtering.
<a id='origin'/>
- **Origin**(`origin` `type:object`) is found in [assessment-results](assessment-results.html) & [poam](poam.html)
  - definition: Identifies the tool or activity that resulted in the observation.
<a id='origination'/>
- **Assessment Origination**(`origination` `type:object`) is found in [assessment-plan](assessment-plan.html) & [assessment-results](assessment-results.html)
  - definition: Identifies the origination of network-based assessment activities, such as the IP address of the tool performing assessment scans.
<a id='oscal-version'/>
- **OSCAL version**(`oscal-version` `type:string`) is found in [assessment-plan](assessment-plan.html), [assessment-results](assessment-results.html), [catalog](catalog.html), [component](component.html), [poam](poam.html), [profile](profile.html) & [ssp](ssp.html)
  - definition: OSCAL model version.
<a id='param'/>
- **Parameter**(`param` `type:object`) is found in [catalog](catalog.html) & [profile](profile.html)
  - definition: Parameters provide a mechanism for the dynamic assignment of value(s) in a control.
<a id='part'/>
- **Part**(`part` `type:object`) is found in [assessment-plan](assessment-plan.html), [assessment-results](assessment-results.html), [catalog](catalog.html) & [profile](profile.html)
  - definition: A partition or component of a control or part
<a id='party'/>
- **Party (organization or person)**(`party` `type:object`) is found in [assessment-plan](assessment-plan.html), [assessment-results](assessment-results.html), [catalog](catalog.html), [component](component.html), [poam](poam.html), [profile](profile.html) & [ssp](ssp.html)
  - definition: A responsible entity, either singular (an organization or person) or collective (multiple persons)
<a id='party-name'/>
- **Party Name**(`party-name` `type:string`) is found in [assessment-plan](assessment-plan.html), [assessment-results](assessment-results.html), [catalog](catalog.html), [component](component.html), [poam](poam.html), [profile](profile.html) & [ssp](ssp.html)
  - definition: The full (legal) name of the party.
<a id='party-uuid'/>
- **Party Reference**(`party-uuid` `type:string`) is found in [assessment-plan](assessment-plan.html), [assessment-results](assessment-results.html), [catalog](catalog.html), [component](component.html), [poam](poam.html), [profile](profile.html) & [ssp](ssp.html)
  - definition: References a party defined in metadata.
<a id='phone'/>
- **Telephone**(`phone` `type:object`) is found in [assessment-plan](assessment-plan.html), [assessment-results](assessment-results.html), [catalog](catalog.html), [component](component.html), [poam](poam.html), [profile](profile.html) & [ssp](ssp.html)
  - definition: Contact number by telephone
<a id='plan-of-action-and-milestones'/>
- **Plan of Action and Milestones (POA&M)**(`plan-of-action-and-milestones` `type:object`) is found in [poam](poam.html)
  - definition: A plan of action and milestones, such as those required by FedRAMP.
<a id='port-range'/>
- **Port Range**(`port-range` `type:object`) is found in [assessment-plan](assessment-plan.html), [assessment-results](assessment-results.html), [poam](poam.html) & [ssp](ssp.html)
  - definition: Where applicable this is the IPv4 port range on which the service operates.
<a id='postal-code'/>
- **Postal Code**(`postal-code` `type:string`) is found in [assessment-plan](assessment-plan.html), [assessment-results](assessment-results.html), [catalog](catalog.html), [component](component.html), [poam](poam.html), [profile](profile.html) & [ssp](ssp.html)
  - definition: Postal or ZIP code for mailing address
<a id='profile'/>
- **Profile**(`profile` `type:object`) is found in [profile](profile.html)
  - definition: Each OSCAL profile is defined by a Profile element
<a id='prop'/>
- **Property**(`prop` `type:object`) is found in [assessment-plan](assessment-plan.html), [assessment-results](assessment-results.html), [catalog](catalog.html), [component](component.html), [poam](poam.html), [profile](profile.html) & [ssp](ssp.html)
  - definition: A value with a name, attributed to the containing control, part, or group.
<a id='prose'/>
- **Prose**(`prose` `type:string`) is found in [assessment-plan](assessment-plan.html), [assessment-results](assessment-results.html), [catalog](catalog.html) & [profile](profile.html)
  - definition: Prose permits multiple paragraphs, lists, tables etc.
<a id='protocol'/>
- **Protocol**(`protocol` `type:object`) is found in [assessment-plan](assessment-plan.html), [assessment-results](assessment-results.html), [poam](poam.html) & [ssp](ssp.html)
  - definition: Information about the protocol used to provide a service.
<a id='published'/>
- **Publication Timestamp**(`published` `type:string`) is found in [assessment-plan](assessment-plan.html), [assessment-results](assessment-results.html), [catalog](catalog.html), [component](component.html), [poam](poam.html), [profile](profile.html) & [ssp](ssp.html)
  - definition: The date and time this document was published.
<a id='purpose'/>
- **Purpose**(`purpose` `type:string`) is found in [assessment-plan](assessment-plan.html), [assessment-results](assessment-results.html), [poam](poam.html) & [ssp](ssp.html)
  - definition: Describes the purpose for the service within the system.
<a id='relevant-evidence'/>
- **Relevant Evidence**(`relevant-evidence` `type:object`) is found in [assessment-results](assessment-results.html) & [poam](poam.html)
  - definition: Links this observation to relevant evidence.
<a id='remarks'/>
- **Remarks**(`remarks` `type:string`) is found in [assessment-plan](assessment-plan.html), [assessment-results](assessment-results.html), [catalog](catalog.html), [component](component.html), [poam](poam.html), [profile](profile.html) & [ssp](ssp.html)
  - definition: Additional commentary on the parent item.
<a id='remediation'/>
- **Remediation**(`remediation` `type:object`) is found in [assessment-results](assessment-results.html) & [poam](poam.html)
  - definition: Describes either recommendation or an actual plan for remediating the risk.
<a id='remediation-origin'/>
- **Remediation Origin**(`remediation-origin` `type:object`) is found in [assessment-results](assessment-results.html) & [poam](poam.html)
  - definition: Points to the source of the remediation recommendation or plan
<a id='remediation-tracking'/>
- **Remediation Tracking**(`remediation-tracking` `type:object`) is found in [assessment-results](assessment-results.html) & [poam](poam.html)
  - definition: A log of events and actions taken towards the remediation of the associated risk.
<a id='remove'/>
- **Removal**(`remove` `type:object`) is found in [profile](profile.html)
  - definition: Specifies elements to be removed from a control, in resolution
<a id='required'/>
- **Required**(`required` `type:object`) is found in [assessment-results](assessment-results.html) & [poam](poam.html)
  - definition: Identifies something required to achieve remediation.
<a id='resource'/>
- **Resource**(`resource` `type:object`) is found in [assessment-plan](assessment-plan.html), [assessment-results](assessment-results.html), [catalog](catalog.html), [component](component.html), [poam](poam.html), [profile](profile.html) & [ssp](ssp.html)
  - definition: A resource associated with the present document, which may be a pointer to other data or a citation.
<a id='responsible-party'/>
- **Responsible Party**(`responsible-party` `type:object`) is found in [assessment-plan](assessment-plan.html), [assessment-results](assessment-results.html), [catalog](catalog.html), [component](component.html), [poam](poam.html), [profile](profile.html) & [ssp](ssp.html)
  - definition: A reference to a set of organizations or persons that have responsibility for performing a referenced role relative to the parent context.
<a id='responsible-role'/>
- **Responsible Role**(`responsible-role` `type:object`) is found in [assessment-plan](assessment-plan.html), [assessment-results](assessment-results.html), [component](component.html), [poam](poam.html) & [ssp](ssp.html)
  - definition: A reference to one or more roles with responsibility for performing a function relative to the control.
<a id='result'/>
- **Result**(`result` `type:object`) is found in [assessment-results](assessment-results.html) & [poam](poam.html)
  - definition: A brief indication as to whether the objective is satisfied or not.
<a id='results'/>
- **Assessment Results**(`results` `type:object`) is found in [assessment-results](assessment-results.html) & [poam](poam.html)
  - definition: Used by the assessment results and POA&M. In the assessment results, this identifies all of the assessment observations and findings, initial and residual risks, deviations, and disposition. In the POA&M, this identifies initial and residual risks, deviations, and disposition.
<a id='revision'/>
- **Revision History Entry**(`revision` `type:object`) is found in [assessment-plan](assessment-plan.html), [assessment-results](assessment-results.html), [catalog](catalog.html), [component](component.html), [poam](poam.html), [profile](profile.html) & [ssp](ssp.html)
  - definition: An entry in a sequential list of revisions to the containing document in reverse chronological order (i.e., most recent previous revision first).
<a id='risk'/>
- **Identified Risk**(`risk` `type:object`) is found in [assessment-results](assessment-results.html) & [poam](poam.html)
  - definition: An identified risk.
<a id='risk-metric'/>
- **Risk Metric**(`risk-metric` `type:object`) is found in [assessment-results](assessment-results.html) & [poam](poam.html)
  - definition: An individual risk metric from a specified system.
<a id='risk-statement'/>
- **Risk Statement**(`risk-statement` `type:string`) is found in [assessment-results](assessment-results.html) & [poam](poam.html)
  - definition: Describes the risk.
<a id='risk-status'/>
- **Status**(`risk-status` `type:string`) is found in [assessment-results](assessment-results.html) & [poam](poam.html)
  - definition: Describes the status of the associated risk.
<a id='rlink'/>
- **Resource link**(`rlink` `type:object`) is found in [assessment-plan](assessment-plan.html), [assessment-results](assessment-results.html), [catalog](catalog.html), [component](component.html), [poam](poam.html), [profile](profile.html) & [ssp](ssp.html)
  - definition: A pointer to an external copy of a document with optional hash for verification
<a id='role'/>
- **Role**(`role` `type:object`) is found in [assessment-plan](assessment-plan.html), [assessment-results](assessment-results.html), [catalog](catalog.html), [component](component.html), [poam](poam.html), [profile](profile.html) & [ssp](ssp.html)
  - definition: Defining a role to be assigned to a party
<a id='role-id'/>
- **Role Identifier Reference**(`role-id` `type:string`) is found in [assessment-plan](assessment-plan.html), [assessment-results](assessment-results.html), [poam](poam.html) & [ssp](ssp.html)
  - definition: A reference to the roles served by the user.
<a id='schedule'/>
- **Schedule**(`schedule` `type:object`) is found in [assessment-plan](assessment-plan.html), [assessment-results](assessment-results.html) & [poam](poam.html)
  - definition: Identifies the schedule for the assessment activities.
<a id='security-impact-level'/>
- **Security Impact Level**(`security-impact-level` `type:object`) is found in [ssp](ssp.html)
  - definition: The overall level of expected impact resulting from unauthorized disclosure, modification, or loss of access to information.
<a id='security-objective-availability'/>
- **Security Objective: Availability**(`security-objective-availability` `type:string`) is found in [ssp](ssp.html)
  - definition: A target-level of availability for the system, based on the sensitivity of information within the system.
<a id='security-objective-confidentiality'/>
- **Security Objective: Confidentiality**(`security-objective-confidentiality` `type:string`) is found in [ssp](ssp.html)
  - definition: A target-level of confidentiality for the system, based on the sensitivity of information within the system.
<a id='security-objective-integrity'/>
- **Security Objective: Integrity**(`security-objective-integrity` `type:string`) is found in [ssp](ssp.html)
  - definition: A target-level of integrity for the system, based on the sensitivity of information within the system.
<a id='security-sensitivity-level'/>
- **Security Sensitivity Level**(`security-sensitivity-level` `type:string`) is found in [ssp](ssp.html)
  - definition: The overall information system sensitivity categorization, such as defined by FIPS-199.
<a id='select'/>
- **Selection**(`select` `type:object`) is found in [catalog](catalog.html) & [profile](profile.html)
  - definition: Presenting a choice among alternatives
<a id='selected'/>
- **Selected Level (Confidentiality, Integrity, or Availability)**(`selected` `type:string`) is found in [ssp](ssp.html)
  - definition: The selected (Confidentiality, Integrity, or Availability) security impact level.
<a id='sequence'/>
- **Sequence Number**(`sequence` `type:integer`) is found in [assessment-plan](assessment-plan.html) & [assessment-results](assessment-results.html)
  - definition: Identifies the sequence number for the test step.
<a id='set-parameter'/>
- **Set Parameter Value**(`set-parameter` `type:object`) is found in [component](component.html), [profile](profile.html) & [ssp](ssp.html)
  - definition for **Set Parameter Value** is different between these schemas
    - component: Identifies the parameter that will be filled in by the enclosed value element.
    - profile: A parameter setting, to be propagated to points of insertion
    - ssp: Identifies the parameter that will be filled in by the enclosed value element.
<a id='short-name'/>
- **short-name**(`short-name` `type:string`) is found in [assessment-plan](assessment-plan.html), [assessment-results](assessment-results.html), [catalog](catalog.html), [component](component.html), [poam](poam.html), [profile](profile.html) & [ssp](ssp.html)
  - definition: A common name, short name or acronym
<a id='start'/>
- **Start**(`start` `type:string`) is found in [assessment-plan](assessment-plan.html), [assessment-results](assessment-results.html) & [poam](poam.html)
  - definition: Identifies the start of a task.
<a id='state'/>
- **State**(`state` `type:string`) is found in [assessment-plan](assessment-plan.html), [assessment-results](assessment-results.html), [catalog](catalog.html), [component](component.html), [poam](poam.html), [profile](profile.html) & [ssp](ssp.html)
  - definition: State, province or analogous geographical region for mailing address
<a id='statement'/>
- **Specific Statement**(`statement` `type:object`) is found in [component](component.html) & [ssp](ssp.html)
  - definition for **Specific Statement** is different between these schemas
    - component: Identifies which statements within a control are addressed.
    - ssp: Identifies which statements within a control are addressed.
<a id='status'/>
- **Status**(`status` `type:object`) is found in [assessment-plan](assessment-plan.html), [assessment-results](assessment-results.html), [poam](poam.html) & [ssp](ssp.html)
  - definition: Describes the operational status of the system.
<a id='subject-reference'/>
- **Identifies the Subject**(`subject-reference` `type:object`) is found in [assessment-plan](assessment-plan.html), [assessment-results](assessment-results.html) & [poam](poam.html)
  - definition: A pointer to a resource based on its ID. Use type to indicate whether the identified resource is a component, inventory item, location, user, or something else.
<a id='system-characteristics'/>
- **System Characteristics**(`system-characteristics` `type:object`) is found in [ssp](ssp.html)
  - definition: Contains the characteristics of the system, such as its name, purpose, and security impact level.
<a id='system-id'/>
- **System Identification**(`system-id` `type:object`) is found in [poam](poam.html) & [ssp](ssp.html)
  - definition: A unique identifier for the system described by this system security plan.
<a id='system-implementation'/>
- **System Implementation**(`system-implementation` `type:object`) is found in [ssp](ssp.html)
  - definition: Provides information as to how the system is implemented.
<a id='system-information'/>
- **System Information**(`system-information` `type:object`) is found in [ssp](ssp.html)
  - definition: Contains details about all information types that are stored, processed, or transmitted by the system, such as privacy information, and those defined in NIST SP 800-60.
<a id='system-inventory'/>
- **System Inventory**(`system-inventory` `type:object`) is found in [ssp](ssp.html)
  - definition: A set of inventory-item entries that represent the managed inventory instances of the system.
<a id='system-name'/>
- **System Name (Full)**(`system-name` `type:string`) is found in [ssp](ssp.html)
  - definition: The full name of the system.
<a id='system-name-short'/>
- **System Name (Short)**(`system-name-short` `type:string`) is found in [ssp](ssp.html)
  - definition: A short name for the system, such as an acronym, that is suitable for display in a data table or summary list.
<a id='system-security-plan'/>
- **System Security Plan (SSP)**(`system-security-plan` `type:object`) is found in [ssp](ssp.html)
  - definition: A system security plan, such as those described in NIST SP 800-18
<a id='task'/>
- **Task**(`task` `type:object`) is found in [assessment-plan](assessment-plan.html), [assessment-results](assessment-results.html) & [poam](poam.html)
  - definition: Identifies an individual task.
<a id='test-method'/>
- **Test Method**(`test-method` `type:object`) is found in [assessment-plan](assessment-plan.html) & [assessment-results](assessment-results.html)
  - definition: Identifies an individual test method.
<a id='test-step'/>
- **Test Steps**(`test-step` `type:object`) is found in [assessment-plan](assessment-plan.html) & [assessment-results](assessment-results.html)
  - definition: Identifies an individual test step.
<a id='text'/>
- **Text**(`text` `type:string`) is found in [assessment-plan](assessment-plan.html), [assessment-results](assessment-results.html), [catalog](catalog.html), [component](component.html), [poam](poam.html), [profile](profile.html) & [ssp](ssp.html)
  - definition: A line of textual content whose semantic is determined by the context of use.
<a id='threat-id'/>
- **Threat ID**(`threat-id` `type:object`) is found in [assessment-results](assessment-results.html) & [poam](poam.html)
  - definition: A pointer, by ID, to an externally-defined threat.
<a id='title'/>
- **Title**(`title` `type:string`) is found in [assessment-plan](assessment-plan.html), [assessment-results](assessment-results.html), [catalog](catalog.html), [component](component.html), [poam](poam.html), [profile](profile.html) & [ssp](ssp.html)
  - definition: A title for display and navigation
<a id='tools'/>
- **Assessment Assets**(`tools` `type:object`) is found in [assessment-plan](assessment-plan.html) & [assessment-results](assessment-results.html)
  - definition: The technology tools used by the assessor to perform the assessment, such as vulnerability scanners. In the assessment plan these are the intended tools. In the assessment results, these are the actual tools used, including any differences from the assessment plan.
<a id='tracking-entry'/>
- **Tracking Entry**(`tracking-entry` `type:object`) is found in [assessment-results](assessment-results.html) & [poam](poam.html)
  - definition: Individual remediation tracking entry, which logs an event or action taken towards the remediation of the associated risk.
<a id='url'/>
- **URL**(`url` `type:string`) is found in [assessment-plan](assessment-plan.html), [assessment-results](assessment-results.html), [catalog](catalog.html), [component](component.html), [poam](poam.html), [profile](profile.html) & [ssp](ssp.html)
  - definition: URL for web site or Internet presence
<a id='usage'/>
- **Parameter description**(`usage` `type:object`) is found in [catalog](catalog.html) & [profile](profile.html)
  - definition: Indicates and explains the purpose and use of a parameter
<a id='user'/>
- **System User Class**(`user` `type:object`) is found in [assessment-plan](assessment-plan.html), [assessment-results](assessment-results.html) & [ssp](ssp.html)
  - definition: A type of user that interacts with the system based on an associated role.
<a id='value'/>
- **Value**(`value` `type:string`) is found in [catalog](catalog.html), [component](component.html), [profile](profile.html) & [ssp](ssp.html)
  - definition for **Value** is different between these schemas
    - catalog: Indicates a permissible value for a parameter or property
    - component: The phrase or string that fills-in the parameter and completes the requirement statement.
    - profile: Indicates a permissible value for a parameter or property
    - ssp: The phrase or string that fills-in the parameter and completes the requirement statement.
<a id='version'/>
- **Document version**(`version` `type:string`) is found in [assessment-plan](assessment-plan.html), [assessment-results](assessment-results.html), [catalog](catalog.html), [component](component.html), [poam](poam.html), [profile](profile.html) & [ssp](ssp.html)
  - definition: The version of the document content.

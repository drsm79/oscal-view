## assessment-plan

> OSCAL Assessment Plan Format

- <a id='assessment-plan-activity_id'>**Activity ID**</a>: Links the task to a defined activity.
```json
{
  "title": "Activity ID",
  "description": "Links the task to a defined activity.",
  "$id": "#/definitions/activity-uuid",
  "type": "string",
  "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
}
```
- <a id='assessment-plan-address_line'>**Address line**</a>: A single line of an address.
```json
{
  "title": "Address line",
  "description": "A single line of an address.",
  "$id": "#/definitions/addr-line",
  "type": "string"
}
```
- <a id='assessment-plan-address'>**Address**</a>: A postal address.
```json
{
  "title": "Address",
  "description": "A postal address.",
  "$id": "#/definitions/address",
  "type": "object",
  "properties": {
    "type": {
      "description": "Indicates the type of address.",
      "type": "string"
    },
    "postal-address": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/addr-line"
      }
    },
    "city": {
      "$ref": "#/definitions/city"
    },
    "state": {
      "$ref": "#/definitions/state"
    },
    "postal-code": {
      "$ref": "#/definitions/postal-code"
    },
    "country": {
      "$ref": "#/definitions/country"
    }
  },
  "additionalProperties": false
}
```
- <a id='assessment-plan-all'>**All**</a>: A key word to indicate all
```json
{
  "title": "All",
  "description": "A key word to indicate all",
  "$id": "#/definitions/all",
  "type": "string"
}
```
- <a id='assessment-plan-annotation'>**Annotation**</a>: A name/value pair with optional explanatory remarks.
```json
{
  "title": "Annotation",
  "description": "A name/value pair with optional explanatory remarks.",
  "$id": "#/definitions/annotation",
  "type": "object",
  "properties": {
    "name": {
      "title": "Name",
      "description": "Identifying the purpose and intended use of the property, part or other object.",
      "type": "string"
    },
    "id": {
      "title": "Identifier",
      "description": "Unique identifier of the containing object",
      "type": "string"
    },
    "ns": {
      "title": "Namespace",
      "description": "A namespace qualifying the name.",
      "type": "string"
    },
    "value": {
      "title": "Value",
      "description": "Indicates the value of the characteristic.",
      "type": "string"
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "name"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-plan-assessment_activities'>**Assessment Activities**</a>: Identifies the assessment activities and schedule. In the assessment plan, these are planned activities. In the assessment results, these are the actual activities performed.
```json
{
  "title": "Assessment Activities",
  "description": "Identifies the assessment activities and schedule. In the assessment plan, these are planned activities. In the assessment results, these are the actual activities performed.",
  "$id": "#/definitions/assessment-activities",
  "type": "object",
  "properties": {
    "test-methods": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/test-method"
      }
    },
    "schedule": {
      "$ref": "#/definitions/schedule"
    },
    "include-activities": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/include-activity"
      }
    },
    "exclude-activities": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/exclude-activity"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "additionalProperties": false
}
```
- <a id='assessment-plan-assessment_method'>**Assessment Method**</a>: Identifies a method for assessing the satisfaction of this objective.
```json
{
  "title": "Assessment Method",
  "description": "Identifies a method for assessing the satisfaction of this objective.",
  "$id": "#/definitions/assessment-method",
  "type": "object",
  "properties": {
    "method-uuid": {
      "title": "Method ID",
      "description": "Identifies the assessment method.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "STRVALUE": {
      "type": "string"
    }
  },
  "required": [
    "STRVALUE",
    "method-uuid"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-plan-security_assessment_plan_(sap)'>**Security Assessment Plan (SAP)**</a>: An assessment plan, such as those provided by a FedRAMP assessor.
```json
{
  "title": "Security Assessment Plan (SAP)",
  "description": "An assessment plan, such as those provided by a FedRAMP assessor.",
  "$id": "#/definitions/assessment-plan",
  "type": "object",
  "properties": {
    "uuid": {
      "title": "Universally Unique Identifier",
      "description": "A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "metadata": {
      "$ref": "#/definitions/metadata"
    },
    "import-ssp": {
      "$ref": "#/definitions/import-ssp"
    },
    "objectives": {
      "$ref": "#/definitions/objectives"
    },
    "assessment-subjects": {
      "$ref": "#/definitions/assessment-subjects"
    },
    "assets": {
      "$ref": "#/definitions/assets"
    },
    "assessment-activities": {
      "$ref": "#/definitions/assessment-activities"
    },
    "back-matter": {
      "$ref": "#/definitions/back-matter"
    }
  },
  "required": [
    "uuid",
    "metadata",
    "import-ssp",
    "objectives"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-plan-subject_of_assessment'>**Subject of Assessment**</a>: Identifies system elements being assessed, such as components, inventory items, and locations. In the assessment plan, this identifies the planned assessment subject. In the assessment results this is the actual assessment subject, and reflects any changes from the plan.
```json
{
  "title": "Subject of Assessment",
  "description": "Identifies system elements being assessed, such as components, inventory items, and locations. In the assessment plan, this identifies the planned assessment subject. In the assessment results this is the actual assessment subject, and reflects any changes from the plan.",
  "$id": "#/definitions/assessment-subjects",
  "type": "object",
  "properties": {
    "includes": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/include-subject"
      }
    },
    "excludes": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/exclude-subject"
      }
    },
    "local-definitions": {
      "$ref": "#/definitions/local-definitions"
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "includes"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-plan-assessment_assets'>**Assessment Assets**</a>: Identifies the assets used to perform this assessment, such as the assessment team, scanning tools, and assumptions.
```json
{
  "title": "Assessment Assets",
  "description": "Identifies the assets used to perform this assessment, such as the assessment team, scanning tools, and assumptions.",
  "$id": "#/definitions/assets",
  "type": "object",
  "properties": {
    "tools": {
      "$ref": "#/definitions/tools"
    },
    "origination": {
      "$ref": "#/definitions/origination"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "parts": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/part"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "additionalProperties": false
}
```
- <a id='assessment-plan-privilege'>**Privilege**</a>: Identifies a specific system privilege held by the user, along with an associated description and/or rationale for the privilege.
```json
{
  "title": "Privilege",
  "description": "Identifies a specific system privilege held by the user, along with an associated description and/or rationale for the privilege.",
  "$id": "#/definitions/authorized-privilege",
  "type": "object",
  "properties": {
    "title": {
      "$ref": "#/definitions/title"
    },
    "description": {
      "$ref": "#/definitions/description"
    },
    "functions-performed": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/function-performed"
      }
    }
  },
  "required": [
    "title",
    "functions-performed"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-plan-back_matter'>**Back matter**</a>: A collection of citations and resource references.
```json
{
  "title": "Back matter",
  "description": "A collection of citations and resource references.",
  "$id": "#/definitions/back-matter",
  "type": "object",
  "properties": {
    "resources": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/resource"
      }
    }
  },
  "additionalProperties": false
}
```
- <a id='assessment-plan-base64'>**Base64**</a>: 
```json
{
  "title": "Base64",
  "description": "",
  "$id": "#/definitions/base64",
  "type": "object",
  "properties": {
    "filename": {
      "title": "File Name",
      "description": "Name of the file before it was encoded as Base64 to be embedded in a resource. This is the name that will be assigned to the file when the file is decoded.",
      "type": "string",
      "format": "uri-reference"
    },
    "media-type": {
      "title": "Media type",
      "description": "Describes the media type of the linked resource",
      "type": "string"
    },
    "value": {
      "type": "string"
    }
  },
  "required": [
    "value"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-plan-bibliographic_definition'>**Bibliographic Definition**</a>: A container in which a set of bibliographic information can included. The model of this information is undefined by OSCAL.
```json
{
  "title": "Bibliographic Definition",
  "description": "A container in which a set of bibliographic information can included. The model of this information is undefined by OSCAL.",
  "$id": "#/definitions/biblio",
  "type": "object",
  "additionalProperties": false
}
```
- <a id='assessment-plan-citation'>**Citation**</a>: A citation consisting of end note text and optional structured bibliographic data.
```json
{
  "title": "Citation",
  "description": "A citation consisting of end note text and optional structured bibliographic data.",
  "$id": "#/definitions/citation",
  "type": "object",
  "properties": {
    "text": {
      "$ref": "#/definitions/text"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "biblio": {
      "$ref": "#/definitions/biblio"
    }
  },
  "required": [
    "text"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-plan-city'>**City**</a>: City, town or geographical region for mailing address
```json
{
  "title": "City",
  "description": "City, town or geographical region for mailing address",
  "$id": "#/definitions/city",
  "type": "string"
}
```
- <a id='assessment-plan-compare_to'>**Compare To**</a>: Typically used in when copying content from the assessment plan to the assessment results. The uuid should be changed in the assessment results file, and the compare-to field should be set to the original assessment plan uuid value. This enables the plan and results to be compared later to identify what changed between the two.
```json
{
  "title": "Compare To",
  "description": "Typically used in when copying content from the assessment plan to the assessment results. The uuid should be changed in the assessment results file, and the compare-to field should be set to the original assessment plan uuid value. This enables the plan and results to be compared later to identify what changed between the two.",
  "$id": "#/definitions/compare-to",
  "type": "string"
}
```
- <a id='assessment-plan-component'>**Component**</a>: A defined component that can be part of an implemented system.
```json
{
  "title": "Component",
  "description": "A defined component that can be part of an implemented system.",
  "$id": "#/definitions/component",
  "type": "object",
  "properties": {
    "component-type": {
      "title": "Component Type",
      "description": "A category describing the purpose of the component.",
      "type": "string"
    },
    "title": {
      "$ref": "#/definitions/title"
    },
    "description": {
      "$ref": "#/definitions/description"
    },
    "purpose": {
      "$ref": "#/definitions/purpose"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "status": {
      "$ref": "#/definitions/status"
    },
    "responsible-roles": {
      "type": "object",
      "minProperties": 1,
      "additionalProperties": {
        "allOf": [
          {
            "type": "object",
            "$ref": "#/definitions/responsible-role"
          },
          {
            "not": {
              "type": "string"
            }
          }
        ]
      }
    },
    "protocols": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/protocol"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "component-type",
    "title",
    "description",
    "status"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-plan-control_objectives'>**Control Objectives**</a>: Identifies the control objectives of the assessment. In the assessment plan, these are the planned objectives. In the assessment results, these are the actual objectives, and reflects any changes from the plan.
```json
{
  "title": "Control Objectives",
  "description": "Identifies the control objectives of the assessment. In the assessment plan, these are the planned objectives. In the assessment results, these are the actual objectives, and reflects any changes from the plan.",
  "$id": "#/definitions/control-objectives",
  "type": "object",
  "properties": {
    "description": {
      "$ref": "#/definitions/description"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "all": {
      "$ref": "#/definitions/all"
    },
    "include-objectives": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/include-objective"
      }
    },
    "exclude-objectives": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/exclude-objective"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "additionalProperties": false
}
```
- <a id='assessment-plan-assessed_controls'>**Assessed Controls**</a>: Identifies the controls being assessed. In the assessment plan, these are the planned controls. In the assessment results, these are the actual controls, and reflects any changes from the plan.
```json
{
  "title": "Assessed Controls",
  "description": "Identifies the controls being assessed. In the assessment plan, these are the planned controls. In the assessment results, these are the actual controls, and reflects any changes from the plan.",
  "$id": "#/definitions/controls",
  "type": "object",
  "properties": {
    "description": {
      "$ref": "#/definitions/description"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "all": {
      "$ref": "#/definitions/all"
    },
    "include-controls": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/include-control"
      }
    },
    "exclude-controls": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/exclude-control"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "additionalProperties": false
}
```
- <a id='assessment-plan-country'>**Country**</a>: Country for mailing address
```json
{
  "title": "Country",
  "description": "Country for mailing address",
  "$id": "#/definitions/country",
  "type": "string"
}
```
- <a id='assessment-plan-description'>**Description**</a>: A short textual description
```json
{
  "title": "Description",
  "description": "A short textual description",
  "$id": "#/definitions/desc",
  "type": "string"
}
```
- <a id='assessment-plan-description'>**Description**</a>: A description supporting the parent item.
```json
{
  "title": "Description",
  "description": "A description supporting the parent item.",
  "$id": "#/definitions/description",
  "type": "string"
}
```
- <a id='assessment-plan-document_identifier'>**Document Identifier**</a>: A document identifier qualified by an identifier type.
```json
{
  "title": "Document Identifier",
  "description": "A document identifier qualified by an identifier type.",
  "$id": "#/definitions/doc-id",
  "type": "object",
  "properties": {
    "type": {
      "description": "Qualifies the kind of document identifier.",
      "type": "string"
    },
    "identifier": {
      "type": "string"
    }
  },
  "required": [
    "identifier",
    "type"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-plan-email'>**Email**</a>: Email address
```json
{
  "title": "Email",
  "description": "Email address",
  "$id": "#/definitions/email",
  "type": "string",
  "format": "email",
  "pattern": "^.+@.+"
}
```
- <a id='assessment-plan-end'>**End**</a>: Identifies the end of a task.
```json
{
  "title": "End",
  "description": "Identifies the end of a task.",
  "$id": "#/definitions/end",
  "type": "string",
  "format": "date-time",
  "pattern": "^((2000|2400|2800|(19|2[0-9](0[48]|[2468][048]|[13579][26])))-02-29)|(((19|2[0-9])[0-9]{2})-02-(0[1-9]|1[0-9]|2[0-8]))|(((19|2[0-9])[0-9]{2})-(0[13578]|10|12)-(0[1-9]|[12][0-9]|3[01]))|(((19|2[0-9])[0-9]{2})-(0[469]|11)-(0[1-9]|[12][0-9]|30))T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\\.[0-9]+)?(Z|[+-][0-9]{2}:[0-9]{2})$"
}
```
- <a id='assessment-plan-included_activity'>**Included Activity**</a>: Identifies an activity explicitly excluded from the assessment. In the assessment plan, this clarifies activities that are out-of-scope or prohibited. In the assessment results, this could be used to explicitly identify an activity that was planned, but not performed.
```json
{
  "title": "Included Activity",
  "description": "Identifies an activity explicitly excluded from the assessment. In the assessment plan, this clarifies activities that are out-of-scope or prohibited. In the assessment results, this could be used to explicitly identify an activity that was planned, but not performed.",
  "$id": "#/definitions/exclude-activity",
  "type": "object",
  "properties": {
    "uuid": {
      "title": "Universally Unique Identifier",
      "description": "A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "title": {
      "$ref": "#/definitions/title"
    },
    "description": {
      "$ref": "#/definitions/description"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "role-ids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/role-id"
      }
    },
    "party-uuids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/party-uuid"
      }
    },
    "location-uuids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/location-uuid"
      }
    },
    "compare-to": {
      "$ref": "#/definitions/compare-to"
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "uuid",
    "description"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-plan-exclude_control'>**Exclude Control**</a>: Identifies an individual control to exclude.
```json
{
  "title": "Exclude Control",
  "description": "Identifies an individual control to exclude.",
  "$id": "#/definitions/exclude-control",
  "type": "object",
  "properties": {
    "control-id": {
      "title": "Control Identifier Reference",
      "description": "A reference to a control identifier.",
      "type": "string"
    },
    "STRVALUE": {
      "type": "string"
    }
  },
  "required": [
    "STRVALUE",
    "control-id"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-plan-exclude_objective'>**Exclude Objective**</a>: Identifies an individual control objective to exclude.
```json
{
  "title": "Exclude Objective",
  "description": "Identifies an individual control objective to exclude.",
  "$id": "#/definitions/exclude-objective",
  "type": "object",
  "properties": {
    "objective-id": {
      "title": "Objective ID",
      "description": "Points to an assessment objective.",
      "type": "string"
    },
    "STRVALUE": {
      "type": "string"
    }
  },
  "required": [
    "STRVALUE",
    "objective-id"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-plan-excluded_assessment_subject'>**Excluded Assessment Subject**</a>: Identifies what is explicitly excluded from this assessment. Used to remove a subset of items from groups of explicitly included items. Also used to explicitly clarify off-limit items, such as hosts to avoid scanning.
```json
{
  "title": "Excluded Assessment Subject",
  "description": "Identifies what is explicitly excluded from this assessment. Used to remove a subset of items from groups of explicitly included items. Also used to explicitly clarify off-limit items, such as hosts to avoid scanning.",
  "$id": "#/definitions/exclude-subject",
  "type": "object",
  "properties": {
    "name": {
      "title": "Name",
      "description": "Identifying the purpose and intended use of the property, part or other object.",
      "type": "string"
    },
    "class": {
      "title": "Class",
      "description": "Indicating the type or classification of the containing object",
      "type": "string"
    },
    "description": {
      "$ref": "#/definitions/description"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "all": {
      "$ref": "#/definitions/all"
    },
    "subject-references": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/subject-reference"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "name",
    "description"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-plan-personal_identifier'>**Personal Identifier**</a>: An identifier for a person (such as an ORCID) using a designated scheme.
```json
{
  "title": "Personal Identifier",
  "description": "An identifier for a person (such as an ORCID) using a designated scheme.",
  "$id": "#/definitions/external-id",
  "type": "object",
  "properties": {
    "type": {
      "title": "Type",
      "description": "Indicating the type of identifier, address, email or other data item.",
      "type": "string"
    },
    "id": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "type"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-plan-functions_performed'>**Functions Performed**</a>: Describes a function performed for a given authorized privilege by this user class.
```json
{
  "title": "Functions Performed",
  "description": "Describes a function performed for a given authorized privilege by this user class.",
  "$id": "#/definitions/function-performed",
  "type": "string"
}
```
- <a id='assessment-plan-hash'>**Hash**</a>: A representation of a cryptographic digest generated over a resource using a hash algorithm.
```json
{
  "title": "Hash",
  "description": "A representation of a cryptographic digest generated over a resource using a hash algorithm.",
  "$id": "#/definitions/hash",
  "type": "object",
  "properties": {
    "algorithm": {
      "title": "Hash algorithm",
      "description": "Method by which a hash is derived",
      "type": "string"
    },
    "value": {
      "type": "string"
    }
  },
  "required": [
    "value",
    "algorithm"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-plan-implemented_component'>**Implemented Component**</a>: The set of componenets that are implemented in a given system inventory item.
```json
{
  "title": "Implemented Component",
  "description": "The set of componenets that are implemented in a given system inventory item.",
  "$id": "#/definitions/implemented-component",
  "type": "object",
  "properties": {
    "use": {
      "title": "Implementation Use Type",
      "description": "The type of implementation",
      "type": "string"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "responsible-parties": {
      "type": "object",
      "minProperties": 1,
      "additionalProperties": {
        "allOf": [
          {
            "type": "object",
            "$ref": "#/definitions/responsible-party"
          },
          {
            "not": {
              "type": "string"
            }
          }
        ]
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "additionalProperties": false
}
```
- <a id='assessment-plan-import_system_security_plan'>**Import System Security Plan**</a>: Used by the assessment plan and POA&M to import information about the system.
```json
{
  "title": "Import System Security Plan",
  "description": "Used by the assessment plan and POA&M to import information about the system.",
  "$id": "#/definitions/import-ssp",
  "type": "object",
  "properties": {
    "href": {
      "title": "hypertext reference",
      "description": "A link to a document or document fragment (actual, nominal or projected)",
      "type": "string",
      "format": "uri-reference"
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "href"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-plan-included_activity'>**Included Activity**</a>: Identifies an assessment activity. In the assessment plan, this is an intended/in-scope activity. In the assessment results, this identifies an activity that was actually performed.
```json
{
  "title": "Included Activity",
  "description": "Identifies an assessment activity. In the assessment plan, this is an intended/in-scope activity. In the assessment results, this identifies an activity that was actually performed.",
  "$id": "#/definitions/include-activity",
  "type": "object",
  "properties": {
    "uuid": {
      "title": "Universally Unique Identifier",
      "description": "A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "title": {
      "$ref": "#/definitions/title"
    },
    "description": {
      "$ref": "#/definitions/description"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "role-ids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/role-id"
      }
    },
    "party-uuids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/party-uuid"
      }
    },
    "location-uuids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/location-uuid"
      }
    },
    "compare-to": {
      "$ref": "#/definitions/compare-to"
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "uuid",
    "description"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-plan-include_control'>**Include Control**</a>: Identifies an individual control to include.
```json
{
  "title": "Include Control",
  "description": "Identifies an individual control to include.",
  "$id": "#/definitions/include-control",
  "type": "object",
  "properties": {
    "control-id": {
      "title": "Control Identifier Reference",
      "description": "A reference to a control identifier.",
      "type": "string"
    },
    "STRVALUE": {
      "type": "string"
    }
  },
  "required": [
    "STRVALUE",
    "control-id"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-plan-include_objective'>**Include Objective**</a>: Identifies an individual control objective to include.
```json
{
  "title": "Include Objective",
  "description": "Identifies an individual control objective to include.",
  "$id": "#/definitions/include-objective",
  "type": "object",
  "properties": {
    "objective-id": {
      "title": "Objective ID",
      "description": "Points to an assessment objective.",
      "type": "string"
    },
    "STRVALUE": {
      "type": "string"
    }
  },
  "required": [
    "STRVALUE",
    "objective-id"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-plan-included_assessment_subject'>**Included Assessment Subject**</a>: Identifies exactly what will be the focus of this assessment. Anything not explicitly defined is out-of-scope.
```json
{
  "title": "Included Assessment Subject",
  "description": "Identifies exactly what will be the focus of this assessment. Anything not explicitly defined is out-of-scope.",
  "$id": "#/definitions/include-subject",
  "type": "object",
  "properties": {
    "name": {
      "title": "Name",
      "description": "Identifying the purpose and intended use of the property, part or other object.",
      "type": "string"
    },
    "class": {
      "title": "Class",
      "description": "Indicating the type or classification of the containing object",
      "type": "string"
    },
    "description": {
      "$ref": "#/definitions/description"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "all": {
      "$ref": "#/definitions/all"
    },
    "subject-references": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/subject-reference"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "name",
    "description"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-plan-inventory_item'>**Inventory Item**</a>: A single managed inventory item within the system.
```json
{
  "title": "Inventory Item",
  "description": "A single managed inventory item within the system.",
  "$id": "#/definitions/inventory-item",
  "type": "object",
  "properties": {
    "asset-id": {
      "title": "Asset Identifier",
      "description": "Organizational asset identifier that is unique in the context of the system. This may be a reference to the identifier used in an asset tracking system or a vulnerability scanning tool.",
      "type": "string"
    },
    "description": {
      "$ref": "#/definitions/description"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "responsible-parties": {
      "type": "object",
      "minProperties": 1,
      "additionalProperties": {
        "allOf": [
          {
            "type": "object",
            "$ref": "#/definitions/responsible-party"
          },
          {
            "not": {
              "type": "string"
            }
          }
        ]
      }
    },
    "implemented-components": {
      "type": "object",
      "minProperties": 1,
      "additionalProperties": {
        "allOf": [
          {
            "type": "object",
            "$ref": "#/definitions/implemented-component"
          },
          {
            "not": {
              "type": "string"
            }
          }
        ]
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "asset-id",
    "description"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-plan-last_modified_timestamp'>**Last modified timestamp**</a>: Date and time of last modification.
```json
{
  "title": "Last modified timestamp",
  "description": "Date and time of last modification.",
  "$id": "#/definitions/last-modified",
  "type": "string",
  "format": "date-time",
  "pattern": "^((2000|2400|2800|(19|2[0-9](0[48]|[2468][048]|[13579][26])))-02-29)|(((19|2[0-9])[0-9]{2})-02-(0[1-9]|1[0-9]|2[0-8]))|(((19|2[0-9])[0-9]{2})-(0[13578]|10|12)-(0[1-9]|[12][0-9]|3[01]))|(((19|2[0-9])[0-9]{2})-(0[469]|11)-(0[1-9]|[12][0-9]|30))T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\\.[0-9]+)?(Z|[+-][0-9]{2}:[0-9]{2})$"
}
```
- <a id='assessment-plan-link'>**Link**</a>: A reference to a local or remote resource
```json
{
  "title": "Link",
  "description": "A reference to a local or remote resource",
  "$id": "#/definitions/link",
  "type": "object",
  "properties": {
    "href": {
      "title": "hypertext reference",
      "description": "A link to a document or document fragment (actual, nominal or projected)",
      "type": "string",
      "format": "uri-reference"
    },
    "rel": {
      "title": "Relation",
      "description": "Describes the type of relationship provided by the link. This can be an indicator of the link's purpose.",
      "type": "string"
    },
    "media-type": {
      "title": "Media type",
      "description": "Describes the media type of the linked resource",
      "type": "string"
    },
    "text": {
      "type": "string"
    }
  },
  "required": [
    "text",
    "href"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-plan-local_definitions'>**Local Definitions**</a>: Allows control objectives, users, components, and inventory-items to be defined within the assessment plan or assessment results for circumstances where they are not appropriately defined in the SSP. NOTE: Use the assessment plan or assessment results metadata to define additional locations if needed.
```json
{
  "title": "Local Definitions",
  "description": "Allows control objectives, users, components, and inventory-items to be defined within the assessment plan or assessment results for circumstances where they are not appropriately defined in the SSP. NOTE: Use the assessment plan or assessment results metadata to define additional locations if needed.",
  "$id": "#/definitions/local-definitions",
  "type": "object",
  "properties": {
    "components": {
      "type": "object",
      "minProperties": 1,
      "additionalProperties": {
        "allOf": [
          {
            "type": "object",
            "$ref": "#/definitions/component"
          },
          {
            "not": {
              "type": "string"
            }
          }
        ]
      }
    },
    "inventory-items": {
      "type": "object",
      "minProperties": 1,
      "additionalProperties": {
        "allOf": [
          {
            "type": "object",
            "$ref": "#/definitions/inventory-item"
          },
          {
            "not": {
              "type": "string"
            }
          }
        ]
      }
    },
    "users": {
      "type": "object",
      "minProperties": 1,
      "additionalProperties": {
        "allOf": [
          {
            "type": "object",
            "$ref": "#/definitions/user"
          },
          {
            "not": {
              "type": "string"
            }
          }
        ]
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "additionalProperties": false
}
```
- <a id='assessment-plan-location'>**Location**</a>: A location, with associated metadata that can be referenced.
```json
{
  "title": "Location",
  "description": "A location, with associated metadata that can be referenced.",
  "$id": "#/definitions/location",
  "type": "object",
  "properties": {
    "uuid": {
      "title": "Universally Unique Identifier",
      "description": "A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "title": {
      "$ref": "#/definitions/title"
    },
    "address": {
      "$ref": "#/definitions/address"
    },
    "email-addresses": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/email"
      }
    },
    "telephone-numbers": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/phone"
      }
    },
    "URLs": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/url"
      }
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "uuid",
    "address"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-plan-location_reference'>**Location Reference**</a>: References a location defined in metadata.
```json
{
  "title": "Location Reference",
  "description": "References a location defined in metadata.",
  "$id": "#/definitions/location-uuid",
  "type": "string",
  "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
}
```
- <a id='assessment-plan-organizational_affiliation'>**Organizational Affiliation**</a>: Identifies that the containing object is a member of the organization associated with the provided UUID.
```json
{
  "title": "Organizational Affiliation",
  "description": "Identifies that the containing object is a member of the organization associated with the provided UUID.",
  "$id": "#/definitions/member-of-organization",
  "type": "string",
  "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
}
```
- <a id='assessment-plan-publication_metadata'>**Publication metadata**</a>: Provides information about the publication and availability of the containing document.
```json
{
  "title": "Publication metadata",
  "description": "Provides information about the publication and availability of the containing document.",
  "$id": "#/definitions/metadata",
  "type": "object",
  "properties": {
    "title": {
      "$ref": "#/definitions/title"
    },
    "published": {
      "$ref": "#/definitions/published"
    },
    "last-modified": {
      "$ref": "#/definitions/last-modified"
    },
    "version": {
      "$ref": "#/definitions/version"
    },
    "oscal-version": {
      "$ref": "#/definitions/oscal-version"
    },
    "revision-history": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/revision"
      }
    },
    "document-ids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/doc-id"
      }
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "roles": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/role"
      }
    },
    "locations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/location"
      }
    },
    "parties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/party"
      }
    },
    "responsible-parties": {
      "type": "object",
      "minProperties": 1,
      "additionalProperties": {
        "allOf": [
          {
            "type": "object",
            "$ref": "#/definitions/responsible-party"
          },
          {
            "not": {
              "type": "string"
            }
          }
        ]
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "title",
    "last-modified",
    "version",
    "oscal-version"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-plan-assessment_method'>**Assessment Method**</a>: A local definition of a control objective. Uses catalog syntax for control objective and assessment actions.
```json
{
  "title": "Assessment Method",
  "description": "A local definition of a control objective. Uses catalog syntax for control objective and assessment actions.",
  "$id": "#/definitions/method",
  "type": "object",
  "properties": {
    "uuid": {
      "title": "Universally Unique Identifier",
      "description": "A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "description": {
      "$ref": "#/definitions/description"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "part": {
      "$ref": "#/definitions/part"
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "uuid",
    "part"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-plan-control_objective'>**Control Objective**</a>: A local definition of a control objective. Uses catalog syntax for control objective and assessment actions.
```json
{
  "title": "Control Objective",
  "description": "A local definition of a control objective. Uses catalog syntax for control objective and assessment actions.",
  "$id": "#/definitions/objective",
  "type": "object",
  "properties": {
    "id": {
      "title": "Identifier",
      "description": "Unique identifier of the containing object",
      "type": "string"
    },
    "control-id": {
      "title": "Control Identifier Reference",
      "description": "A reference to a control identifier.",
      "type": "string"
    },
    "description": {
      "$ref": "#/definitions/description"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "part": {
      "$ref": "#/definitions/part"
    },
    "methods": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/assessment-method"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "id",
    "control-id",
    "part"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-plan-objectives_of_assessment'>**Objectives of Assessment**</a>: Identifies the controls and control being assessed and their control objectives. In the assessment plans, these are the planned controls and objectives. In the assessment results, these are the actual controls and objectives, and reflects any changes from the plan.
```json
{
  "title": "Objectives of Assessment",
  "description": "Identifies the controls and control being assessed and their control objectives. In the assessment plans, these are the planned controls and objectives. In the assessment results, these are the actual controls and objectives, and reflects any changes from the plan.",
  "$id": "#/definitions/objectives",
  "type": "object",
  "properties": {
    "description": {
      "$ref": "#/definitions/description"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "control-group": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/controls"
      }
    },
    "control-objective-group": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/control-objectives"
      }
    },
    "objective": {
      "$ref": "#/definitions/objective"
    },
    "method-definitions": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/method"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "control-group"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-plan-assessment_origination'>**Assessment Origination**</a>: Identifies the origination of network-based assessment activities, such as the IP address of the tool performing assessment scans.
```json
{
  "title": "Assessment Origination",
  "description": "Identifies the origination of network-based assessment activities, such as the IP address of the tool performing assessment scans.",
  "$id": "#/definitions/origination",
  "type": "object",
  "properties": {
    "title": {
      "$ref": "#/definitions/title"
    },
    "description": {
      "$ref": "#/definitions/description"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    }
  },
  "required": [
    "title"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-plan-oscal_version'>**OSCAL version**</a>: OSCAL model version.
```json
{
  "title": "OSCAL version",
  "description": "OSCAL model version.",
  "$id": "#/definitions/oscal-version",
  "type": "string"
}
```
- <a id='assessment-plan-part'>**Part**</a>: A partition or component of a control or part
```json
{
  "title": "Part",
  "description": "A partition or component of a control or part",
  "$id": "#/definitions/part",
  "type": "object",
  "properties": {
    "id": {
      "title": "Identifier",
      "description": "Unique identifier of the containing object",
      "type": "string"
    },
    "name": {
      "title": "Name",
      "description": "Identifying the purpose and intended use of the property, part or other object.",
      "type": "string"
    },
    "ns": {
      "title": "Namespace",
      "description": "A namespace qualifying the name.",
      "type": "string"
    },
    "class": {
      "title": "Class",
      "description": "Indicating the type or classification of the containing object",
      "type": "string"
    },
    "title": {
      "$ref": "#/definitions/title"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "prose": {
      "$ref": "#/definitions/prose"
    },
    "parts": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/part"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    }
  },
  "required": [
    "name"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-plan-party_(organization_or_person)'>**Party (organization or person)**</a>: A responsible entity, either singular (an organization or person) or collective (multiple persons)
```json
{
  "title": "Party (organization or person)",
  "description": "A responsible entity, either singular (an organization or person) or collective (multiple persons)",
  "$id": "#/definitions/party",
  "type": "object",
  "properties": {
    "uuid": {
      "title": "Universally Unique Identifier",
      "description": "A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "type": {
      "title": "Party Type",
      "description": "A category describing the kind of party the object describes.",
      "type": "string",
      "enum": [
        "person",
        "organization"
      ]
    },
    "party-name": {
      "$ref": "#/definitions/party-name"
    },
    "short-name": {
      "$ref": "#/definitions/short-name"
    },
    "external-ids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/external-id"
      }
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "addresses": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/address"
      }
    },
    "email-addresses": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/email"
      }
    },
    "telephone-numbers": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/phone"
      }
    },
    "member-of-organizations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/member-of-organization"
      }
    },
    "location-uuids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/location-uuid"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "uuid",
    "type",
    "party-name"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-plan-party_name'>**Party Name**</a>: The full (legal) name of the party.
```json
{
  "title": "Party Name",
  "description": "The full (legal) name of the party.",
  "$id": "#/definitions/party-name",
  "type": "string"
}
```
- <a id='assessment-plan-party_reference'>**Party Reference**</a>: References a party defined in metadata.
```json
{
  "title": "Party Reference",
  "description": "References a party defined in metadata.",
  "$id": "#/definitions/party-uuid",
  "type": "string",
  "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
}
```
- <a id='assessment-plan-telephone'>**Telephone**</a>: Contact number by telephone
```json
{
  "title": "Telephone",
  "description": "Contact number by telephone",
  "$id": "#/definitions/phone",
  "type": "object",
  "properties": {
    "type": {
      "description": "Indicates the type of phone number.",
      "type": "string"
    },
    "number": {
      "type": "string"
    }
  },
  "required": [
    "number"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-plan-port_range'>**Port Range**</a>: Where applicable this is the IPv4 port range on which the service operates.
```json
{
  "title": "Port Range",
  "description": "Where applicable this is the IPv4 port range on which the service operates.",
  "$id": "#/definitions/port-range",
  "type": "object",
  "properties": {
    "start": {
      "title": "Start",
      "description": "Indicates the starting port number in a port range",
      "type": "integer",
      "multipleOf": 1,
      "minimum": 0
    },
    "end": {
      "title": "End",
      "description": "Indicates the ending port number in a port range",
      "type": "integer",
      "multipleOf": 1,
      "minimum": 0
    },
    "transport": {
      "title": "Transport",
      "description": "Indicates the transport type.",
      "type": "string",
      "enum": [
        "TCP",
        "UDP"
      ]
    }
  },
  "additionalProperties": false
}
```
- <a id='assessment-plan-postal_code'>**Postal Code**</a>: Postal or ZIP code for mailing address
```json
{
  "title": "Postal Code",
  "description": "Postal or ZIP code for mailing address",
  "$id": "#/definitions/postal-code",
  "type": "string"
}
```
- <a id='assessment-plan-property'>**Property**</a>: A value with a name, attributed to the containing control, part, or group.
```json
{
  "title": "Property",
  "description": "A value with a name, attributed to the containing control, part, or group.",
  "$id": "#/definitions/prop",
  "type": "object",
  "properties": {
    "name": {
      "title": "Name",
      "description": "Identifying the purpose and intended use of the property, part or other object.",
      "type": "string"
    },
    "id": {
      "title": "Identifier",
      "description": "Unique identifier of the containing object",
      "type": "string"
    },
    "ns": {
      "title": "Namespace",
      "description": "A namespace qualifying the name.",
      "type": "string"
    },
    "class": {
      "title": "Class",
      "description": "Indicating the type or classification of the containing object",
      "type": "string"
    },
    "value": {
      "type": "string"
    }
  },
  "required": [
    "value",
    "name"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-plan-prose'>**Prose**</a>: Prose permits multiple paragraphs, lists, tables etc.
```json
{
  "title": "Prose",
  "description": "Prose permits multiple paragraphs, lists, tables etc.",
  "$id": "#/definitions/prose",
  "type": "string"
}
```
- <a id='assessment-plan-protocol'>**Protocol**</a>: Information about the protocol used to provide a service.
```json
{
  "title": "Protocol",
  "description": "Information about the protocol used to provide a service.",
  "$id": "#/definitions/protocol",
  "type": "object",
  "properties": {
    "uuid": {
      "title": "Universally Unique Identifier",
      "description": "A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "name": {
      "description": "The short name of the protocol (e.g., TLS).",
      "type": "string"
    },
    "title": {
      "$ref": "#/definitions/title"
    },
    "port-ranges": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/port-range"
      }
    }
  },
  "required": [
    "name"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-plan-publication_timestamp'>**Publication Timestamp**</a>: The date and time this document was published.
```json
{
  "title": "Publication Timestamp",
  "description": "The date and time this document was published.",
  "$id": "#/definitions/published",
  "type": "string",
  "format": "date-time",
  "pattern": "^((2000|2400|2800|(19|2[0-9](0[48]|[2468][048]|[13579][26])))-02-29)|(((19|2[0-9])[0-9]{2})-02-(0[1-9]|1[0-9]|2[0-8]))|(((19|2[0-9])[0-9]{2})-(0[13578]|10|12)-(0[1-9]|[12][0-9]|3[01]))|(((19|2[0-9])[0-9]{2})-(0[469]|11)-(0[1-9]|[12][0-9]|30))T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\\.[0-9]+)?(Z|[+-][0-9]{2}:[0-9]{2})$"
}
```
- <a id='assessment-plan-purpose'>**Purpose**</a>: Describes the purpose for the service within the system.
```json
{
  "title": "Purpose",
  "description": "Describes the purpose for the service within the system.",
  "$id": "#/definitions/purpose",
  "type": "string"
}
```
- <a id='assessment-plan-remarks'>**Remarks**</a>: Additional commentary on the parent item.
```json
{
  "title": "Remarks",
  "description": "Additional commentary on the parent item.",
  "$id": "#/definitions/remarks",
  "type": "string"
}
```
- <a id='assessment-plan-resource'>**Resource**</a>: A resource associated with the present document, which may be a pointer to other data or a citation.
```json
{
  "title": "Resource",
  "description": "A resource associated with the present document, which may be a pointer to other data or a citation.",
  "$id": "#/definitions/resource",
  "type": "object",
  "properties": {
    "uuid": {
      "title": "Universally Unique Identifier",
      "description": "A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "title": {
      "$ref": "#/definitions/title"
    },
    "desc": {
      "$ref": "#/definitions/desc"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "document-ids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/doc-id"
      }
    },
    "citation": {
      "$ref": "#/definitions/citation"
    },
    "rlinks": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/rlink"
      }
    },
    "attachments": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/base64"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "uuid"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-plan-responsible_party'>**Responsible Party**</a>: A reference to a set of organizations or persons that have responsibility for performing a referenced role relative to the parent context.
```json
{
  "title": "Responsible Party",
  "description": "A reference to a set of organizations or persons that have responsibility for performing a referenced role relative to the parent context.",
  "$id": "#/definitions/responsible-party",
  "type": "object",
  "properties": {
    "party-uuids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/party-uuid"
      }
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "party-uuids"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-plan-responsible_role'>**Responsible Role**</a>: A reference to one or more roles with responsibility for performing a function relative to the control.
```json
{
  "title": "Responsible Role",
  "description": "A reference to one or more roles with responsibility for performing a function relative to the control.",
  "$id": "#/definitions/responsible-role",
  "type": "object",
  "properties": {
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "party-ids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/party-uuid"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "additionalProperties": false
}
```
- <a id='assessment-plan-revision_history_entry'>**Revision History Entry**</a>: An entry in a sequential list of revisions to the containing document in reverse chronological order (i.e., most recent previous revision first).
```json
{
  "title": "Revision History Entry",
  "description": "An entry in a sequential list of revisions to the containing document in reverse chronological order (i.e., most recent previous revision first).",
  "$id": "#/definitions/revision",
  "type": "object",
  "properties": {
    "title": {
      "$ref": "#/definitions/title"
    },
    "published": {
      "$ref": "#/definitions/published"
    },
    "last-modified": {
      "$ref": "#/definitions/last-modified"
    },
    "version": {
      "$ref": "#/definitions/version"
    },
    "oscal-version": {
      "$ref": "#/definitions/oscal-version"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "additionalProperties": false
}
```
- <a id='assessment-plan-resource_link'>**Resource link**</a>: A pointer to an external copy of a document with optional hash for verification
```json
{
  "title": "Resource link",
  "description": "A pointer to an external copy of a document with optional hash for verification",
  "$id": "#/definitions/rlink",
  "type": "object",
  "properties": {
    "href": {
      "title": "hypertext reference",
      "description": "A link to a document or document fragment (actual, nominal or projected)",
      "type": "string",
      "format": "uri-reference"
    },
    "media-type": {
      "title": "Media type",
      "description": "Describes the media type of the linked resource",
      "type": "string"
    },
    "hashes": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/hash"
      }
    }
  },
  "required": [
    "href"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-plan-role'>**Role**</a>: Defining a role to be assigned to a party
```json
{
  "title": "Role",
  "description": "Defining a role to be assigned to a party",
  "$id": "#/definitions/role",
  "type": "object",
  "properties": {
    "id": {
      "title": "Identifier",
      "description": "Unique identifier of the containing object",
      "type": "string"
    },
    "title": {
      "$ref": "#/definitions/title"
    },
    "short-name": {
      "$ref": "#/definitions/short-name"
    },
    "desc": {
      "$ref": "#/definitions/desc"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "id",
    "title"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-plan-role_identifier_reference'>**Role Identifier Reference**</a>: A reference to the roles served by the user.
```json
{
  "title": "Role Identifier Reference",
  "description": "A reference to the roles served by the user.",
  "$id": "#/definitions/role-id",
  "type": "string"
}
```
- <a id='assessment-plan-schedule'>**Schedule**</a>: Identifies the schedule for the assessment activities.
```json
{
  "title": "Schedule",
  "description": "Identifies the schedule for the assessment activities.",
  "$id": "#/definitions/schedule",
  "type": "object",
  "properties": {
    "uuid": {
      "title": "Universally Unique Identifier",
      "description": "A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "tasks": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/task"
      }
    }
  },
  "required": [
    "tasks"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-plan-sequence_number'>**Sequence Number**</a>: Identifies the sequence number for the test step.
```json
{
  "title": "Sequence Number",
  "description": "Identifies the sequence number for the test step.",
  "$id": "#/definitions/sequence",
  "type": "integer"
}
```
- <a id='assessment-plan-short-name'>**short-name**</a>: A common name, short name or acronym
```json
{
  "title": "short-name",
  "description": "A common name, short name or acronym",
  "$id": "#/definitions/short-name",
  "type": "string"
}
```
- <a id='assessment-plan-start'>**Start**</a>: Identifies the start of a task.
```json
{
  "title": "Start",
  "description": "Identifies the start of a task.",
  "$id": "#/definitions/start",
  "type": "string",
  "format": "date-time",
  "pattern": "^((2000|2400|2800|(19|2[0-9](0[48]|[2468][048]|[13579][26])))-02-29)|(((19|2[0-9])[0-9]{2})-02-(0[1-9]|1[0-9]|2[0-8]))|(((19|2[0-9])[0-9]{2})-(0[13578]|10|12)-(0[1-9]|[12][0-9]|3[01]))|(((19|2[0-9])[0-9]{2})-(0[469]|11)-(0[1-9]|[12][0-9]|30))T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\\.[0-9]+)?(Z|[+-][0-9]{2}:[0-9]{2})$"
}
```
- <a id='assessment-plan-state'>**State**</a>: State, province or analogous geographical region for mailing address
```json
{
  "title": "State",
  "description": "State, province or analogous geographical region for mailing address",
  "$id": "#/definitions/state",
  "type": "string"
}
```
- <a id='assessment-plan-status'>**Status**</a>: Describes the operational status of the system.
```json
{
  "title": "Status",
  "description": "Describes the operational status of the system.",
  "$id": "#/definitions/status",
  "type": "object",
  "properties": {
    "state": {
      "title": "State",
      "description": "The current operating status.",
      "type": "string",
      "enum": [
        "operational",
        "under-development",
        "under-major-modification",
        "disposition",
        "other"
      ]
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "state"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-plan-identifies_the_subject'>**Identifies the Subject**</a>: A pointer to a resource based on its ID. Use type to indicate whether the identified resource is a component, inventory item, location, user, or something else.
```json
{
  "title": "Identifies the Subject",
  "description": "A pointer to a resource based on its ID. Use type to indicate whether the identified resource is a component, inventory item, location, user, or something else.",
  "$id": "#/definitions/subject-reference",
  "type": "object",
  "properties": {
    "uuid-ref": {
      "title": "UUID Reference",
      "description": "A pointer to a component, inventory-item, location, party, user, or resource using it's UUID.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "type": {
      "title": "Type",
      "description": "Indicating the type of identifier, address, email or other data item.",
      "type": "string"
    },
    "title": {
      "$ref": "#/definitions/title"
    },
    "props": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    }
  },
  "required": [
    "uuid-ref",
    "type"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-plan-task'>**Task**</a>: Identifies an individual task.
```json
{
  "title": "Task",
  "description": "Identifies an individual task.",
  "$id": "#/definitions/task",
  "type": "object",
  "properties": {
    "uuid": {
      "title": "Universally Unique Identifier",
      "description": "A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "title": {
      "$ref": "#/definitions/title"
    },
    "description": {
      "$ref": "#/definitions/description"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "start": {
      "$ref": "#/definitions/start"
    },
    "end": {
      "$ref": "#/definitions/end"
    },
    "activity-uuids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/activity-uuid"
      }
    },
    "role-ids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/role-id"
      }
    },
    "party-uuids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/party-uuid"
      }
    },
    "location-uuids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/location-uuid"
      }
    },
    "compare-to": {
      "$ref": "#/definitions/compare-to"
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "uuid"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-plan-test_method'>**Test Method**</a>: Identifies an individual test method.
```json
{
  "title": "Test Method",
  "description": "Identifies an individual test method.",
  "$id": "#/definitions/test-method",
  "type": "object",
  "properties": {
    "uuid": {
      "title": "Universally Unique Identifier",
      "description": "A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "title": {
      "$ref": "#/definitions/title"
    },
    "description": {
      "$ref": "#/definitions/description"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "test-steps": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/test-step"
      }
    },
    "compare-to": {
      "$ref": "#/definitions/compare-to"
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "uuid"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-plan-test_steps'>**Test Steps**</a>: Identifies an individual test step.
```json
{
  "title": "Test Steps",
  "description": "Identifies an individual test step.",
  "$id": "#/definitions/test-step",
  "type": "object",
  "properties": {
    "uuid": {
      "title": "Universally Unique Identifier",
      "description": "A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "sequence": {
      "$ref": "#/definitions/sequence"
    },
    "description": {
      "$ref": "#/definitions/description"
    },
    "role-ids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/role-id"
      }
    },
    "party-uuids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/party-uuid"
      }
    },
    "compare-to": {
      "$ref": "#/definitions/compare-to"
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "uuid",
    "description"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-plan-text'>**Text**</a>: A line of textual content whose semantic is determined by the context of use.
```json
{
  "title": "Text",
  "description": "A line of textual content whose semantic is determined by the context of use.",
  "$id": "#/definitions/text",
  "type": "string"
}
```
- <a id='assessment-plan-title'>**Title**</a>: A title for display and navigation
```json
{
  "title": "Title",
  "description": "A title for display and navigation",
  "$id": "#/definitions/title",
  "type": "string"
}
```
- <a id='assessment-plan-assessment_assets'>**Assessment Assets**</a>: The technology tools used by the assessor to perform the assessment, such as vulnerability scanners. In the assessment plan these are the intended tools. In the assessment results, these are the actual tools used, including any differences from the assessment plan.
```json
{
  "title": "Assessment Assets",
  "description": "The technology tools used by the assessor to perform the assessment, such as vulnerability scanners. In the assessment plan these are the intended tools. In the assessment results, these are the actual tools used, including any differences from the assessment plan.",
  "$id": "#/definitions/tools",
  "type": "object",
  "properties": {
    "components": {
      "type": "object",
      "minProperties": 1,
      "additionalProperties": {
        "allOf": [
          {
            "type": "object",
            "$ref": "#/definitions/component"
          },
          {
            "not": {
              "type": "string"
            }
          }
        ]
      }
    }
  },
  "additionalProperties": false
}
```
- <a id='assessment-plan-url'>**URL**</a>: URL for web site or Internet presence
```json
{
  "title": "URL",
  "description": "URL for web site or Internet presence",
  "$id": "#/definitions/url",
  "type": "string",
  "format": "uri"
}
```
- <a id='assessment-plan-system_user_class'>**System User Class**</a>: A type of user that interacts with the system based on an associated role.
```json
{
  "title": "System User Class",
  "description": "A type of user that interacts with the system based on an associated role.",
  "$id": "#/definitions/user",
  "type": "object",
  "properties": {
    "title": {
      "$ref": "#/definitions/title"
    },
    "short-name": {
      "$ref": "#/definitions/short-name"
    },
    "description": {
      "$ref": "#/definitions/description"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "role-ids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/role-id"
      }
    },
    "authorized-privileges": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/authorized-privilege"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "role-ids"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-plan-document_version'>**Document version**</a>: The version of the document content.
```json
{
  "title": "Document version",
  "description": "The version of the document content.",
  "$id": "#/definitions/version",
  "type": "string"
}
```

## assessment-results

> OSCAL Assessment Results Format

- <a id='assessment-results-activity_id'>**Activity ID**</a>: Links the task to a defined activity.
```json
{
  "title": "Activity ID",
  "description": "Links the task to a defined activity.",
  "$id": "#/definitions/activity-uuid",
  "type": "string",
  "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
}
```
- <a id='assessment-results-address_line'>**Address line**</a>: A single line of an address.
```json
{
  "title": "Address line",
  "description": "A single line of an address.",
  "$id": "#/definitions/addr-line",
  "type": "string"
}
```
- <a id='assessment-results-address'>**Address**</a>: A postal address.
```json
{
  "title": "Address",
  "description": "A postal address.",
  "$id": "#/definitions/address",
  "type": "object",
  "properties": {
    "type": {
      "description": "Indicates the type of address.",
      "type": "string"
    },
    "postal-address": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/addr-line"
      }
    },
    "city": {
      "$ref": "#/definitions/city"
    },
    "state": {
      "$ref": "#/definitions/state"
    },
    "postal-code": {
      "$ref": "#/definitions/postal-code"
    },
    "country": {
      "$ref": "#/definitions/country"
    }
  },
  "additionalProperties": false
}
```
- <a id='assessment-results-all'>**All**</a>: A key word to indicate all
```json
{
  "title": "All",
  "description": "A key word to indicate all",
  "$id": "#/definitions/all",
  "type": "string"
}
```
- <a id='assessment-results-annotation'>**Annotation**</a>: A name/value pair with optional explanatory remarks.
```json
{
  "title": "Annotation",
  "description": "A name/value pair with optional explanatory remarks.",
  "$id": "#/definitions/annotation",
  "type": "object",
  "properties": {
    "name": {
      "title": "Name",
      "description": "Identifying the purpose and intended use of the property, part or other object.",
      "type": "string"
    },
    "id": {
      "title": "Identifier",
      "description": "Unique identifier of the containing object",
      "type": "string"
    },
    "ns": {
      "title": "Namespace",
      "description": "A namespace qualifying the name.",
      "type": "string"
    },
    "value": {
      "title": "Value",
      "description": "Indicates the value of the characteristic.",
      "type": "string"
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "name"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-results-assessment_activities'>**Assessment Activities**</a>: Identifies the assessment activities and schedule. In the assessment plan, these are planned activities. In the assessment results, these are the actual activities performed.
```json
{
  "title": "Assessment Activities",
  "description": "Identifies the assessment activities and schedule. In the assessment plan, these are planned activities. In the assessment results, these are the actual activities performed.",
  "$id": "#/definitions/assessment-activities",
  "type": "object",
  "properties": {
    "test-methods": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/test-method"
      }
    },
    "schedule": {
      "$ref": "#/definitions/schedule"
    },
    "include-activities": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/include-activity"
      }
    },
    "exclude-activities": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/exclude-activity"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "additionalProperties": false
}
```
- <a id='assessment-results-assessment_method'>**Assessment Method**</a>: Identifies a method for assessing the satisfaction of this objective.
```json
{
  "title": "Assessment Method",
  "description": "Identifies a method for assessing the satisfaction of this objective.",
  "$id": "#/definitions/assessment-method",
  "type": "object",
  "properties": {
    "method-uuid": {
      "title": "Method ID",
      "description": "Identifies the assessment method.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "STRVALUE": {
      "type": "string"
    }
  },
  "required": [
    "STRVALUE",
    "method-uuid"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-results-security_assessment_results_(sar)'>**Security Assessment Results (SAR)**</a>: Security assessment results, such as those provided by a FedRAMP assessor in the FedRAMP Security Assessment Report.
```json
{
  "title": "Security Assessment Results (SAR)",
  "description": "Security assessment results, such as those provided by a FedRAMP assessor in the FedRAMP Security Assessment Report.",
  "$id": "#/definitions/assessment-results",
  "type": "object",
  "properties": {
    "uuid": {
      "title": "Universally Unique Identifier",
      "description": "A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "metadata": {
      "$ref": "#/definitions/metadata"
    },
    "import-ap": {
      "$ref": "#/definitions/import-ap"
    },
    "objectives": {
      "$ref": "#/definitions/objectives"
    },
    "assessment-subjects": {
      "$ref": "#/definitions/assessment-subjects"
    },
    "assets": {
      "$ref": "#/definitions/assets"
    },
    "assessment-activities": {
      "$ref": "#/definitions/assessment-activities"
    },
    "results_group": {
      "anyOf": [
        {
          "$ref": "#/definitions/results"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/results"
          },
          "minItems": 2
        }
      ]
    },
    "back-matter": {
      "$ref": "#/definitions/back-matter"
    }
  },
  "required": [
    "uuid",
    "metadata",
    "import-ap",
    "objectives",
    "results_group"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-results-subject_of_assessment'>**Subject of Assessment**</a>: Identifies system elements being assessed, such as components, inventory items, and locations. In the assessment plan, this identifies the planned assessment subject. In the assessment results this is the actual assessment subject, and reflects any changes from the plan.
```json
{
  "title": "Subject of Assessment",
  "description": "Identifies system elements being assessed, such as components, inventory items, and locations. In the assessment plan, this identifies the planned assessment subject. In the assessment results this is the actual assessment subject, and reflects any changes from the plan.",
  "$id": "#/definitions/assessment-subjects",
  "type": "object",
  "properties": {
    "includes": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/include-subject"
      }
    },
    "excludes": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/exclude-subject"
      }
    },
    "local-definitions": {
      "$ref": "#/definitions/local-definitions"
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "includes"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-results-assessor'>**Assessor**</a>: Identifies an individual who gathered the evidence resulting in the observation or risk identification.
```json
{
  "title": "Assessor",
  "description": "Identifies an individual who gathered the evidence resulting in the observation or risk identification.",
  "$id": "#/definitions/assessor",
  "type": "object",
  "properties": {
    "party-uuid": {
      "title": "Party UUID",
      "description": "The UUID of the assessor who collected the evidence or made the observation.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "STRVALUE": {
      "type": "string"
    }
  },
  "required": [
    "STRVALUE",
    "party-uuid"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-results-assessment_assets'>**Assessment Assets**</a>: Identifies the assets used to perform this assessment, such as the assessment team, scanning tools, and assumptions.
```json
{
  "title": "Assessment Assets",
  "description": "Identifies the assets used to perform this assessment, such as the assessment team, scanning tools, and assumptions.",
  "$id": "#/definitions/assets",
  "type": "object",
  "properties": {
    "tools": {
      "$ref": "#/definitions/tools"
    },
    "origination": {
      "$ref": "#/definitions/origination"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "parts": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/part"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "additionalProperties": false
}
```
- <a id='assessment-results-privilege'>**Privilege**</a>: Identifies a specific system privilege held by the user, along with an associated description and/or rationale for the privilege.
```json
{
  "title": "Privilege",
  "description": "Identifies a specific system privilege held by the user, along with an associated description and/or rationale for the privilege.",
  "$id": "#/definitions/authorized-privilege",
  "type": "object",
  "properties": {
    "title": {
      "$ref": "#/definitions/title"
    },
    "description": {
      "$ref": "#/definitions/description"
    },
    "functions-performed": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/function-performed"
      }
    }
  },
  "required": [
    "title",
    "functions-performed"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-results-back_matter'>**Back matter**</a>: A collection of citations and resource references.
```json
{
  "title": "Back matter",
  "description": "A collection of citations and resource references.",
  "$id": "#/definitions/back-matter",
  "type": "object",
  "properties": {
    "resources": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/resource"
      }
    }
  },
  "additionalProperties": false
}
```
- <a id='assessment-results-base64'>**Base64**</a>: 
```json
{
  "title": "Base64",
  "description": "",
  "$id": "#/definitions/base64",
  "type": "object",
  "properties": {
    "filename": {
      "title": "File Name",
      "description": "Name of the file before it was encoded as Base64 to be embedded in a resource. This is the name that will be assigned to the file when the file is decoded.",
      "type": "string",
      "format": "uri-reference"
    },
    "media-type": {
      "title": "Media type",
      "description": "Describes the media type of the linked resource",
      "type": "string"
    },
    "value": {
      "type": "string"
    }
  },
  "required": [
    "value"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-results-bibliographic_definition'>**Bibliographic Definition**</a>: A container in which a set of bibliographic information can included. The model of this information is undefined by OSCAL.
```json
{
  "title": "Bibliographic Definition",
  "description": "A container in which a set of bibliographic information can included. The model of this information is undefined by OSCAL.",
  "$id": "#/definitions/biblio",
  "type": "object",
  "additionalProperties": false
}
```
- <a id='assessment-results-citation'>**Citation**</a>: A citation consisting of end note text and optional structured bibliographic data.
```json
{
  "title": "Citation",
  "description": "A citation consisting of end note text and optional structured bibliographic data.",
  "$id": "#/definitions/citation",
  "type": "object",
  "properties": {
    "text": {
      "$ref": "#/definitions/text"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "biblio": {
      "$ref": "#/definitions/biblio"
    }
  },
  "required": [
    "text"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-results-city'>**City**</a>: City, town or geographical region for mailing address
```json
{
  "title": "City",
  "description": "City, town or geographical region for mailing address",
  "$id": "#/definitions/city",
  "type": "string"
}
```
- <a id='assessment-results-closer_actions'>**Closer Actions**</a>: Describes the actions taken that resulted in the closure of the identified risk.
```json
{
  "title": "Closer Actions",
  "description": "Describes the actions taken that resulted in the closure of the identified risk.",
  "$id": "#/definitions/closure-actions",
  "type": "string"
}
```
- <a id='assessment-results-compare_to'>**Compare To**</a>: Typically used in when copying content from the assessment plan to the assessment results. The uuid should be changed in the assessment results file, and the compare-to field should be set to the original assessment plan uuid value. This enables the plan and results to be compared later to identify what changed between the two.
```json
{
  "title": "Compare To",
  "description": "Typically used in when copying content from the assessment plan to the assessment results. The uuid should be changed in the assessment results file, and the compare-to field should be set to the original assessment plan uuid value. This enables the plan and results to be compared later to identify what changed between the two.",
  "$id": "#/definitions/compare-to",
  "type": "string"
}
```
- <a id='assessment-results-component'>**Component**</a>: A defined component that can be part of an implemented system.
```json
{
  "title": "Component",
  "description": "A defined component that can be part of an implemented system.",
  "$id": "#/definitions/component",
  "type": "object",
  "properties": {
    "component-type": {
      "title": "Component Type",
      "description": "A category describing the purpose of the component.",
      "type": "string"
    },
    "title": {
      "$ref": "#/definitions/title"
    },
    "description": {
      "$ref": "#/definitions/description"
    },
    "purpose": {
      "$ref": "#/definitions/purpose"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "status": {
      "$ref": "#/definitions/status"
    },
    "responsible-roles": {
      "type": "object",
      "minProperties": 1,
      "additionalProperties": {
        "allOf": [
          {
            "type": "object",
            "$ref": "#/definitions/responsible-role"
          },
          {
            "not": {
              "type": "string"
            }
          }
        ]
      }
    },
    "protocols": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/protocol"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "component-type",
    "title",
    "description",
    "status"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-results-control_objectives'>**Control Objectives**</a>: Identifies the control objectives of the assessment. In the assessment plan, these are the planned objectives. In the assessment results, these are the actual objectives, and reflects any changes from the plan.
```json
{
  "title": "Control Objectives",
  "description": "Identifies the control objectives of the assessment. In the assessment plan, these are the planned objectives. In the assessment results, these are the actual objectives, and reflects any changes from the plan.",
  "$id": "#/definitions/control-objectives",
  "type": "object",
  "properties": {
    "description": {
      "$ref": "#/definitions/description"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "all": {
      "$ref": "#/definitions/all"
    },
    "include-objectives": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/include-objective"
      }
    },
    "exclude-objectives": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/exclude-objective"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "additionalProperties": false
}
```
- <a id='assessment-results-assessed_controls'>**Assessed Controls**</a>: Identifies the controls being assessed. In the assessment plan, these are the planned controls. In the assessment results, these are the actual controls, and reflects any changes from the plan.
```json
{
  "title": "Assessed Controls",
  "description": "Identifies the controls being assessed. In the assessment plan, these are the planned controls. In the assessment results, these are the actual controls, and reflects any changes from the plan.",
  "$id": "#/definitions/controls",
  "type": "object",
  "properties": {
    "description": {
      "$ref": "#/definitions/description"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "all": {
      "$ref": "#/definitions/all"
    },
    "include-controls": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/include-control"
      }
    },
    "exclude-controls": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/exclude-control"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "additionalProperties": false
}
```
- <a id='assessment-results-country'>**Country**</a>: Country for mailing address
```json
{
  "title": "Country",
  "description": "Country for mailing address",
  "$id": "#/definitions/country",
  "type": "string"
}
```
- <a id='assessment-results-date/time_stamp'>**Date/Time Stamp**</a>: Date/time stamp identifying when the information was collected.
```json
{
  "title": "Date/Time Stamp",
  "description": "Date/time stamp identifying when the information was collected.",
  "$id": "#/definitions/date-time-stamp",
  "type": "string",
  "format": "date-time",
  "pattern": "^((2000|2400|2800|(19|2[0-9](0[48]|[2468][048]|[13579][26])))-02-29)|(((19|2[0-9])[0-9]{2})-02-(0[1-9]|1[0-9]|2[0-8]))|(((19|2[0-9])[0-9]{2})-(0[13578]|10|12)-(0[1-9]|[12][0-9]|3[01]))|(((19|2[0-9])[0-9]{2})-(0[469]|11)-(0[1-9]|[12][0-9]|30))T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\\.[0-9]+)?(Z|[+-][0-9]{2}:[0-9]{2})$"
}
```
- <a id='assessment-results-description'>**Description**</a>: A short textual description
```json
{
  "title": "Description",
  "description": "A short textual description",
  "$id": "#/definitions/desc",
  "type": "string"
}
```
- <a id='assessment-results-description'>**Description**</a>: A description supporting the parent item.
```json
{
  "title": "Description",
  "description": "A description supporting the parent item.",
  "$id": "#/definitions/description",
  "type": "string"
}
```
- <a id='assessment-results-document_identifier'>**Document Identifier**</a>: A document identifier qualified by an identifier type.
```json
{
  "title": "Document Identifier",
  "description": "A document identifier qualified by an identifier type.",
  "$id": "#/definitions/doc-id",
  "type": "object",
  "properties": {
    "type": {
      "description": "Qualifies the kind of document identifier.",
      "type": "string"
    },
    "identifier": {
      "type": "string"
    }
  },
  "required": [
    "identifier",
    "type"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-results-email'>**Email**</a>: Email address
```json
{
  "title": "Email",
  "description": "Email address",
  "$id": "#/definitions/email",
  "type": "string",
  "format": "email",
  "pattern": "^.+@.+"
}
```
- <a id='assessment-results-end'>**End**</a>: Identifies the end of a task.
```json
{
  "title": "End",
  "description": "Identifies the end of a task.",
  "$id": "#/definitions/end",
  "type": "string",
  "format": "date-time",
  "pattern": "^((2000|2400|2800|(19|2[0-9](0[48]|[2468][048]|[13579][26])))-02-29)|(((19|2[0-9])[0-9]{2})-02-(0[1-9]|1[0-9]|2[0-8]))|(((19|2[0-9])[0-9]{2})-(0[13578]|10|12)-(0[1-9]|[12][0-9]|3[01]))|(((19|2[0-9])[0-9]{2})-(0[469]|11)-(0[1-9]|[12][0-9]|30))T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\\.[0-9]+)?(Z|[+-][0-9]{2}:[0-9]{2})$"
}
```
- <a id='assessment-results-included_activity'>**Included Activity**</a>: Identifies an activity explicitly excluded from the assessment. In the assessment plan, this clarifies activities that are out-of-scope or prohibited. In the assessment results, this could be used to explicitly identify an activity that was planned, but not performed.
```json
{
  "title": "Included Activity",
  "description": "Identifies an activity explicitly excluded from the assessment. In the assessment plan, this clarifies activities that are out-of-scope or prohibited. In the assessment results, this could be used to explicitly identify an activity that was planned, but not performed.",
  "$id": "#/definitions/exclude-activity",
  "type": "object",
  "properties": {
    "uuid": {
      "title": "Universally Unique Identifier",
      "description": "A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "title": {
      "$ref": "#/definitions/title"
    },
    "description": {
      "$ref": "#/definitions/description"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "role-ids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/role-id"
      }
    },
    "party-uuids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/party-uuid"
      }
    },
    "location-uuids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/location-uuid"
      }
    },
    "compare-to": {
      "$ref": "#/definitions/compare-to"
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "uuid",
    "description"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-results-exclude_control'>**Exclude Control**</a>: Identifies an individual control to exclude.
```json
{
  "title": "Exclude Control",
  "description": "Identifies an individual control to exclude.",
  "$id": "#/definitions/exclude-control",
  "type": "object",
  "properties": {
    "control-id": {
      "title": "Control Identifier Reference",
      "description": "A reference to a control identifier.",
      "type": "string"
    },
    "STRVALUE": {
      "type": "string"
    }
  },
  "required": [
    "STRVALUE",
    "control-id"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-results-exclude_objective'>**Exclude Objective**</a>: Identifies an individual control objective to exclude.
```json
{
  "title": "Exclude Objective",
  "description": "Identifies an individual control objective to exclude.",
  "$id": "#/definitions/exclude-objective",
  "type": "object",
  "properties": {
    "objective-id": {
      "title": "Objective ID",
      "description": "Points to an assessment objective.",
      "type": "string"
    },
    "STRVALUE": {
      "type": "string"
    }
  },
  "required": [
    "STRVALUE",
    "objective-id"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-results-excluded_assessment_subject'>**Excluded Assessment Subject**</a>: Identifies what is explicitly excluded from this assessment. Used to remove a subset of items from groups of explicitly included items. Also used to explicitly clarify off-limit items, such as hosts to avoid scanning.
```json
{
  "title": "Excluded Assessment Subject",
  "description": "Identifies what is explicitly excluded from this assessment. Used to remove a subset of items from groups of explicitly included items. Also used to explicitly clarify off-limit items, such as hosts to avoid scanning.",
  "$id": "#/definitions/exclude-subject",
  "type": "object",
  "properties": {
    "name": {
      "title": "Name",
      "description": "Identifying the purpose and intended use of the property, part or other object.",
      "type": "string"
    },
    "class": {
      "title": "Class",
      "description": "Indicating the type or classification of the containing object",
      "type": "string"
    },
    "description": {
      "$ref": "#/definitions/description"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "all": {
      "$ref": "#/definitions/all"
    },
    "subject-references": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/subject-reference"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "name",
    "description"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-results-personal_identifier'>**Personal Identifier**</a>: An identifier for a person (such as an ORCID) using a designated scheme.
```json
{
  "title": "Personal Identifier",
  "description": "An identifier for a person (such as an ORCID) using a designated scheme.",
  "$id": "#/definitions/external-id",
  "type": "object",
  "properties": {
    "type": {
      "title": "Type",
      "description": "Indicating the type of identifier, address, email or other data item.",
      "type": "string"
    },
    "id": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "type"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-results-finding'>**Finding**</a>: Describes an individual finding.
```json
{
  "title": "Finding",
  "description": "Describes an individual finding.",
  "$id": "#/definitions/finding",
  "type": "object",
  "properties": {
    "uuid": {
      "title": "Universally Unique Identifier",
      "description": "A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "title": {
      "$ref": "#/definitions/title"
    },
    "description": {
      "$ref": "#/definitions/description"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "date-time-stamp": {
      "$ref": "#/definitions/date-time-stamp"
    },
    "objective-status": {
      "$ref": "#/definitions/objective-status"
    },
    "implementation-statement-uuid": {
      "$ref": "#/definitions/implementation-statement-uuid"
    },
    "observations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/observation"
      }
    },
    "threat-ids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/threat-id"
      }
    },
    "risks": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/risk"
      }
    },
    "party-uuids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/party-uuid"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "uuid",
    "title",
    "description",
    "date-time-stamp"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-results-functions_performed'>**Functions Performed**</a>: Describes a function performed for a given authorized privilege by this user class.
```json
{
  "title": "Functions Performed",
  "description": "Describes a function performed for a given authorized privilege by this user class.",
  "$id": "#/definitions/function-performed",
  "type": "string"
}
```
- <a id='assessment-results-hash'>**Hash**</a>: A representation of a cryptographic digest generated over a resource using a hash algorithm.
```json
{
  "title": "Hash",
  "description": "A representation of a cryptographic digest generated over a resource using a hash algorithm.",
  "$id": "#/definitions/hash",
  "type": "object",
  "properties": {
    "algorithm": {
      "title": "Hash algorithm",
      "description": "Method by which a hash is derived",
      "type": "string"
    },
    "value": {
      "type": "string"
    }
  },
  "required": [
    "value",
    "algorithm"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-results-implementation_statement_uuid'>**Implementation Statement UUID**</a>: Identifies the implementation statement in the SSP to which this finding is related.
```json
{
  "title": "Implementation Statement UUID",
  "description": "Identifies the implementation statement in the SSP to which this finding is related.",
  "$id": "#/definitions/implementation-statement-uuid",
  "type": "string",
  "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
}
```
- <a id='assessment-results-implementation_status'>**Implementation Status**</a>: Identifies the implementation status of the control or control objective.
```json
{
  "title": "Implementation Status",
  "description": "Identifies the implementation status of the control or control objective.",
  "$id": "#/definitions/implementation-status",
  "type": "object",
  "properties": {
    "system": {
      "title": "Assessment System",
      "description": "Identifies the framework or rules to which this value conforms.",
      "type": "string",
      "format": "uri"
    },
    "STRVALUE": {
      "type": "string"
    }
  },
  "required": [
    "STRVALUE"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-results-implemented_component'>**Implemented Component**</a>: The set of componenets that are implemented in a given system inventory item.
```json
{
  "title": "Implemented Component",
  "description": "The set of componenets that are implemented in a given system inventory item.",
  "$id": "#/definitions/implemented-component",
  "type": "object",
  "properties": {
    "use": {
      "title": "Implementation Use Type",
      "description": "The type of implementation",
      "type": "string"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "responsible-parties": {
      "type": "object",
      "minProperties": 1,
      "additionalProperties": {
        "allOf": [
          {
            "type": "object",
            "$ref": "#/definitions/responsible-party"
          },
          {
            "not": {
              "type": "string"
            }
          }
        ]
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "additionalProperties": false
}
```
- <a id='assessment-results-import_assessment_plan'>**Import Assessment Plan**</a>: Used by assessment-results to import information about the original plan for assessing the system.
```json
{
  "title": "Import Assessment Plan",
  "description": "Used by assessment-results to import information about the original plan for assessing the system.",
  "$id": "#/definitions/import-ap",
  "type": "object",
  "properties": {
    "href": {
      "title": "hypertext reference",
      "description": "A link to a document or document fragment (actual, nominal or projected)",
      "type": "string",
      "format": "uri-reference"
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "href"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-results-included_activity'>**Included Activity**</a>: Identifies an assessment activity. In the assessment plan, this is an intended/in-scope activity. In the assessment results, this identifies an activity that was actually performed.
```json
{
  "title": "Included Activity",
  "description": "Identifies an assessment activity. In the assessment plan, this is an intended/in-scope activity. In the assessment results, this identifies an activity that was actually performed.",
  "$id": "#/definitions/include-activity",
  "type": "object",
  "properties": {
    "uuid": {
      "title": "Universally Unique Identifier",
      "description": "A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "title": {
      "$ref": "#/definitions/title"
    },
    "description": {
      "$ref": "#/definitions/description"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "role-ids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/role-id"
      }
    },
    "party-uuids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/party-uuid"
      }
    },
    "location-uuids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/location-uuid"
      }
    },
    "compare-to": {
      "$ref": "#/definitions/compare-to"
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "uuid",
    "description"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-results-include_control'>**Include Control**</a>: Identifies an individual control to include.
```json
{
  "title": "Include Control",
  "description": "Identifies an individual control to include.",
  "$id": "#/definitions/include-control",
  "type": "object",
  "properties": {
    "control-id": {
      "title": "Control Identifier Reference",
      "description": "A reference to a control identifier.",
      "type": "string"
    },
    "STRVALUE": {
      "type": "string"
    }
  },
  "required": [
    "STRVALUE",
    "control-id"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-results-include_objective'>**Include Objective**</a>: Identifies an individual control objective to include.
```json
{
  "title": "Include Objective",
  "description": "Identifies an individual control objective to include.",
  "$id": "#/definitions/include-objective",
  "type": "object",
  "properties": {
    "objective-id": {
      "title": "Objective ID",
      "description": "Points to an assessment objective.",
      "type": "string"
    },
    "STRVALUE": {
      "type": "string"
    }
  },
  "required": [
    "STRVALUE",
    "objective-id"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-results-included_assessment_subject'>**Included Assessment Subject**</a>: Identifies exactly what will be the focus of this assessment. Anything not explicitly defined is out-of-scope.
```json
{
  "title": "Included Assessment Subject",
  "description": "Identifies exactly what will be the focus of this assessment. Anything not explicitly defined is out-of-scope.",
  "$id": "#/definitions/include-subject",
  "type": "object",
  "properties": {
    "name": {
      "title": "Name",
      "description": "Identifying the purpose and intended use of the property, part or other object.",
      "type": "string"
    },
    "class": {
      "title": "Class",
      "description": "Indicating the type or classification of the containing object",
      "type": "string"
    },
    "description": {
      "$ref": "#/definitions/description"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "all": {
      "$ref": "#/definitions/all"
    },
    "subject-references": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/subject-reference"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "name",
    "description"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-results-inventory_item'>**Inventory Item**</a>: A single managed inventory item within the system.
```json
{
  "title": "Inventory Item",
  "description": "A single managed inventory item within the system.",
  "$id": "#/definitions/inventory-item",
  "type": "object",
  "properties": {
    "asset-id": {
      "title": "Asset Identifier",
      "description": "Organizational asset identifier that is unique in the context of the system. This may be a reference to the identifier used in an asset tracking system or a vulnerability scanning tool.",
      "type": "string"
    },
    "description": {
      "$ref": "#/definitions/description"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "responsible-parties": {
      "type": "object",
      "minProperties": 1,
      "additionalProperties": {
        "allOf": [
          {
            "type": "object",
            "$ref": "#/definitions/responsible-party"
          },
          {
            "not": {
              "type": "string"
            }
          }
        ]
      }
    },
    "implemented-components": {
      "type": "object",
      "minProperties": 1,
      "additionalProperties": {
        "allOf": [
          {
            "type": "object",
            "$ref": "#/definitions/implemented-component"
          },
          {
            "not": {
              "type": "string"
            }
          }
        ]
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "asset-id",
    "description"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-results-last_modified_timestamp'>**Last modified timestamp**</a>: Date and time of last modification.
```json
{
  "title": "Last modified timestamp",
  "description": "Date and time of last modification.",
  "$id": "#/definitions/last-modified",
  "type": "string",
  "format": "date-time",
  "pattern": "^((2000|2400|2800|(19|2[0-9](0[48]|[2468][048]|[13579][26])))-02-29)|(((19|2[0-9])[0-9]{2})-02-(0[1-9]|1[0-9]|2[0-8]))|(((19|2[0-9])[0-9]{2})-(0[13578]|10|12)-(0[1-9]|[12][0-9]|3[01]))|(((19|2[0-9])[0-9]{2})-(0[469]|11)-(0[1-9]|[12][0-9]|30))T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\\.[0-9]+)?(Z|[+-][0-9]{2}:[0-9]{2})$"
}
```
- <a id='assessment-results-link'>**Link**</a>: A reference to a local or remote resource
```json
{
  "title": "Link",
  "description": "A reference to a local or remote resource",
  "$id": "#/definitions/link",
  "type": "object",
  "properties": {
    "href": {
      "title": "hypertext reference",
      "description": "A link to a document or document fragment (actual, nominal or projected)",
      "type": "string",
      "format": "uri-reference"
    },
    "rel": {
      "title": "Relation",
      "description": "Describes the type of relationship provided by the link. This can be an indicator of the link's purpose.",
      "type": "string"
    },
    "media-type": {
      "title": "Media type",
      "description": "Describes the media type of the linked resource",
      "type": "string"
    },
    "text": {
      "type": "string"
    }
  },
  "required": [
    "text",
    "href"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-results-local_definitions'>**Local Definitions**</a>: Allows control objectives, users, components, and inventory-items to be defined within the assessment plan or assessment results for circumstances where they are not appropriately defined in the SSP. NOTE: Use the assessment plan or assessment results metadata to define additional locations if needed.
```json
{
  "title": "Local Definitions",
  "description": "Allows control objectives, users, components, and inventory-items to be defined within the assessment plan or assessment results for circumstances where they are not appropriately defined in the SSP. NOTE: Use the assessment plan or assessment results metadata to define additional locations if needed.",
  "$id": "#/definitions/local-definitions",
  "type": "object",
  "properties": {
    "components": {
      "type": "object",
      "minProperties": 1,
      "additionalProperties": {
        "allOf": [
          {
            "type": "object",
            "$ref": "#/definitions/component"
          },
          {
            "not": {
              "type": "string"
            }
          }
        ]
      }
    },
    "inventory-items": {
      "type": "object",
      "minProperties": 1,
      "additionalProperties": {
        "allOf": [
          {
            "type": "object",
            "$ref": "#/definitions/inventory-item"
          },
          {
            "not": {
              "type": "string"
            }
          }
        ]
      }
    },
    "users": {
      "type": "object",
      "minProperties": 1,
      "additionalProperties": {
        "allOf": [
          {
            "type": "object",
            "$ref": "#/definitions/user"
          },
          {
            "not": {
              "type": "string"
            }
          }
        ]
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "additionalProperties": false
}
```
- <a id='assessment-results-location'>**Location**</a>: A location, with associated metadata that can be referenced.
```json
{
  "title": "Location",
  "description": "A location, with associated metadata that can be referenced.",
  "$id": "#/definitions/location",
  "type": "object",
  "properties": {
    "uuid": {
      "title": "Universally Unique Identifier",
      "description": "A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "title": {
      "$ref": "#/definitions/title"
    },
    "address": {
      "$ref": "#/definitions/address"
    },
    "email-addresses": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/email"
      }
    },
    "telephone-numbers": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/phone"
      }
    },
    "URLs": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/url"
      }
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "uuid",
    "address"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-results-location_reference'>**Location Reference**</a>: References a location defined in metadata.
```json
{
  "title": "Location Reference",
  "description": "References a location defined in metadata.",
  "$id": "#/definitions/location-uuid",
  "type": "string",
  "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
}
```
- <a id='assessment-results-organizational_affiliation'>**Organizational Affiliation**</a>: Identifies that the containing object is a member of the organization associated with the provided UUID.
```json
{
  "title": "Organizational Affiliation",
  "description": "Identifies that the containing object is a member of the organization associated with the provided UUID.",
  "$id": "#/definitions/member-of-organization",
  "type": "string",
  "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
}
```
- <a id='assessment-results-publication_metadata'>**Publication metadata**</a>: Provides information about the publication and availability of the containing document.
```json
{
  "title": "Publication metadata",
  "description": "Provides information about the publication and availability of the containing document.",
  "$id": "#/definitions/metadata",
  "type": "object",
  "properties": {
    "title": {
      "$ref": "#/definitions/title"
    },
    "published": {
      "$ref": "#/definitions/published"
    },
    "last-modified": {
      "$ref": "#/definitions/last-modified"
    },
    "version": {
      "$ref": "#/definitions/version"
    },
    "oscal-version": {
      "$ref": "#/definitions/oscal-version"
    },
    "revision-history": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/revision"
      }
    },
    "document-ids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/doc-id"
      }
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "roles": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/role"
      }
    },
    "locations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/location"
      }
    },
    "parties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/party"
      }
    },
    "responsible-parties": {
      "type": "object",
      "minProperties": 1,
      "additionalProperties": {
        "allOf": [
          {
            "type": "object",
            "$ref": "#/definitions/responsible-party"
          },
          {
            "not": {
              "type": "string"
            }
          }
        ]
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "title",
    "last-modified",
    "version",
    "oscal-version"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-results-assessment_method'>**Assessment Method**</a>: A local definition of a control objective. Uses catalog syntax for control objective and assessment actions.
```json
{
  "title": "Assessment Method",
  "description": "A local definition of a control objective. Uses catalog syntax for control objective and assessment actions.",
  "$id": "#/definitions/method",
  "type": "object",
  "properties": {
    "uuid": {
      "title": "Universally Unique Identifier",
      "description": "A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "description": {
      "$ref": "#/definitions/description"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "part": {
      "$ref": "#/definitions/part"
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "uuid",
    "part"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-results-mitigating_factor'>**Mitigating Factor**</a>: Describes a mitigating factor with an optional link to an implementation statement in the SSP.
```json
{
  "title": "Mitigating Factor",
  "description": "Describes a mitigating factor with an optional link to an implementation statement in the SSP.",
  "$id": "#/definitions/mitigating-factor",
  "type": "object",
  "properties": {
    "uuid": {
      "title": "Universally Unique Identifier",
      "description": "A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "implementation-uuid": {
      "title": "Implementation UUID",
      "description": "Points to an implementation statement in the SSP.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "description": {
      "$ref": "#/definitions/description"
    },
    "subject-references": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/subject-reference"
      }
    }
  },
  "required": [
    "uuid",
    "description"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-results-control_objective'>**Control Objective**</a>: A local definition of a control objective. Uses catalog syntax for control objective and assessment actions.
```json
{
  "title": "Control Objective",
  "description": "A local definition of a control objective. Uses catalog syntax for control objective and assessment actions.",
  "$id": "#/definitions/objective",
  "type": "object",
  "properties": {
    "id": {
      "title": "Identifier",
      "description": "Unique identifier of the containing object",
      "type": "string"
    },
    "control-id": {
      "title": "Control Identifier Reference",
      "description": "A reference to a control identifier.",
      "type": "string"
    },
    "description": {
      "$ref": "#/definitions/description"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "part": {
      "$ref": "#/definitions/part"
    },
    "methods": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/assessment-method"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "id",
    "control-id",
    "part"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-results-implementation_status'>**Implementation Status**</a>: Captures an assessors conclusions as to whether an objective is fully satisfied.
```json
{
  "title": "Implementation Status",
  "description": "Captures an assessors conclusions as to whether an objective is fully satisfied.",
  "$id": "#/definitions/objective-status",
  "type": "object",
  "properties": {
    "objective-id": {
      "title": "Objective ID",
      "description": "Points to an assessment objective.",
      "type": "string"
    },
    "control-id": {
      "title": "Control Identifier Reference",
      "description": "A reference to a control identifier.",
      "type": "string"
    },
    "title": {
      "$ref": "#/definitions/title"
    },
    "description": {
      "$ref": "#/definitions/description"
    },
    "result": {
      "$ref": "#/definitions/result"
    },
    "implementation-status": {
      "$ref": "#/definitions/implementation-status"
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "additionalProperties": false
}
```
- <a id='assessment-results-objectives_of_assessment'>**Objectives of Assessment**</a>: Identifies the controls and control being assessed and their control objectives. In the assessment plans, these are the planned controls and objectives. In the assessment results, these are the actual controls and objectives, and reflects any changes from the plan.
```json
{
  "title": "Objectives of Assessment",
  "description": "Identifies the controls and control being assessed and their control objectives. In the assessment plans, these are the planned controls and objectives. In the assessment results, these are the actual controls and objectives, and reflects any changes from the plan.",
  "$id": "#/definitions/objectives",
  "type": "object",
  "properties": {
    "description": {
      "$ref": "#/definitions/description"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "control-group": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/controls"
      }
    },
    "control-objective-group": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/control-objectives"
      }
    },
    "objective": {
      "$ref": "#/definitions/objective"
    },
    "method-definitions": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/method"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "control-group"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-results-objective'>**Objective**</a>: Describes an individual observation.
```json
{
  "title": "Objective",
  "description": "Describes an individual observation.",
  "$id": "#/definitions/observation",
  "type": "object",
  "properties": {
    "uuid": {
      "title": "Universally Unique Identifier",
      "description": "A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "title": {
      "$ref": "#/definitions/title"
    },
    "description": {
      "$ref": "#/definitions/description"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "observation-methods": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/observation-method"
      }
    },
    "observation-types": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/observation-type"
      }
    },
    "assessors": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/assessor"
      }
    },
    "subject-references": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/subject-reference"
      }
    },
    "origins": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/origin"
      }
    },
    "evidence-group": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/relevant-evidence"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "uuid",
    "description",
    "observation-methods"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-results-observation_method'>**Observation Method**</a>: Identifies how the observation was made.
```json
{
  "title": "Observation Method",
  "description": "Identifies how the observation was made.",
  "$id": "#/definitions/observation-method",
  "type": "string"
}
```
- <a id='assessment-results-observation_type'>**Observation Type**</a>: Identifies the nature of the observation. More than one may be used to further qualify and enable filtering.
```json
{
  "title": "Observation Type",
  "description": "Identifies the nature of the observation. More than one may be used to further qualify and enable filtering.",
  "$id": "#/definitions/observation-type",
  "type": "string"
}
```
- <a id='assessment-results-origin'>**Origin**</a>: Identifies the tool or activity that resulted in the observation.
```json
{
  "title": "Origin",
  "description": "Identifies the tool or activity that resulted in the observation.",
  "$id": "#/definitions/origin",
  "type": "object",
  "properties": {
    "uuid-ref": {
      "title": "UUID Reference",
      "description": "A pointer to a relevant item, using it's UUID.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "type": {
      "title": "Type",
      "description": "Indicating the type of identifier, address, email or other data item.",
      "type": "string",
      "enum": [
        "tool",
        "test-method",
        "task",
        "included-activity",
        "other"
      ]
    },
    "STRVALUE": {
      "type": "string"
    }
  },
  "required": [
    "STRVALUE",
    "uuid-ref",
    "type"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-results-assessment_origination'>**Assessment Origination**</a>: Identifies the origination of network-based assessment activities, such as the IP address of the tool performing assessment scans.
```json
{
  "title": "Assessment Origination",
  "description": "Identifies the origination of network-based assessment activities, such as the IP address of the tool performing assessment scans.",
  "$id": "#/definitions/origination",
  "type": "object",
  "properties": {
    "title": {
      "$ref": "#/definitions/title"
    },
    "description": {
      "$ref": "#/definitions/description"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    }
  },
  "required": [
    "title"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-results-oscal_version'>**OSCAL version**</a>: OSCAL model version.
```json
{
  "title": "OSCAL version",
  "description": "OSCAL model version.",
  "$id": "#/definitions/oscal-version",
  "type": "string"
}
```
- <a id='assessment-results-part'>**Part**</a>: A partition or component of a control or part
```json
{
  "title": "Part",
  "description": "A partition or component of a control or part",
  "$id": "#/definitions/part",
  "type": "object",
  "properties": {
    "id": {
      "title": "Identifier",
      "description": "Unique identifier of the containing object",
      "type": "string"
    },
    "name": {
      "title": "Name",
      "description": "Identifying the purpose and intended use of the property, part or other object.",
      "type": "string"
    },
    "ns": {
      "title": "Namespace",
      "description": "A namespace qualifying the name.",
      "type": "string"
    },
    "class": {
      "title": "Class",
      "description": "Indicating the type or classification of the containing object",
      "type": "string"
    },
    "title": {
      "$ref": "#/definitions/title"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "prose": {
      "$ref": "#/definitions/prose"
    },
    "parts": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/part"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    }
  },
  "required": [
    "name"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-results-party_(organization_or_person)'>**Party (organization or person)**</a>: A responsible entity, either singular (an organization or person) or collective (multiple persons)
```json
{
  "title": "Party (organization or person)",
  "description": "A responsible entity, either singular (an organization or person) or collective (multiple persons)",
  "$id": "#/definitions/party",
  "type": "object",
  "properties": {
    "uuid": {
      "title": "Universally Unique Identifier",
      "description": "A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "type": {
      "title": "Party Type",
      "description": "A category describing the kind of party the object describes.",
      "type": "string",
      "enum": [
        "person",
        "organization"
      ]
    },
    "party-name": {
      "$ref": "#/definitions/party-name"
    },
    "short-name": {
      "$ref": "#/definitions/short-name"
    },
    "external-ids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/external-id"
      }
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "addresses": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/address"
      }
    },
    "email-addresses": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/email"
      }
    },
    "telephone-numbers": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/phone"
      }
    },
    "member-of-organizations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/member-of-organization"
      }
    },
    "location-uuids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/location-uuid"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "uuid",
    "type",
    "party-name"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-results-party_name'>**Party Name**</a>: The full (legal) name of the party.
```json
{
  "title": "Party Name",
  "description": "The full (legal) name of the party.",
  "$id": "#/definitions/party-name",
  "type": "string"
}
```
- <a id='assessment-results-party_reference'>**Party Reference**</a>: References a party defined in metadata.
```json
{
  "title": "Party Reference",
  "description": "References a party defined in metadata.",
  "$id": "#/definitions/party-uuid",
  "type": "string",
  "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
}
```
- <a id='assessment-results-telephone'>**Telephone**</a>: Contact number by telephone
```json
{
  "title": "Telephone",
  "description": "Contact number by telephone",
  "$id": "#/definitions/phone",
  "type": "object",
  "properties": {
    "type": {
      "description": "Indicates the type of phone number.",
      "type": "string"
    },
    "number": {
      "type": "string"
    }
  },
  "required": [
    "number"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-results-port_range'>**Port Range**</a>: Where applicable this is the IPv4 port range on which the service operates.
```json
{
  "title": "Port Range",
  "description": "Where applicable this is the IPv4 port range on which the service operates.",
  "$id": "#/definitions/port-range",
  "type": "object",
  "properties": {
    "start": {
      "title": "Start",
      "description": "Indicates the starting port number in a port range",
      "type": "integer",
      "multipleOf": 1,
      "minimum": 0
    },
    "end": {
      "title": "End",
      "description": "Indicates the ending port number in a port range",
      "type": "integer",
      "multipleOf": 1,
      "minimum": 0
    },
    "transport": {
      "title": "Transport",
      "description": "Indicates the transport type.",
      "type": "string",
      "enum": [
        "TCP",
        "UDP"
      ]
    }
  },
  "additionalProperties": false
}
```
- <a id='assessment-results-postal_code'>**Postal Code**</a>: Postal or ZIP code for mailing address
```json
{
  "title": "Postal Code",
  "description": "Postal or ZIP code for mailing address",
  "$id": "#/definitions/postal-code",
  "type": "string"
}
```
- <a id='assessment-results-property'>**Property**</a>: A value with a name, attributed to the containing control, part, or group.
```json
{
  "title": "Property",
  "description": "A value with a name, attributed to the containing control, part, or group.",
  "$id": "#/definitions/prop",
  "type": "object",
  "properties": {
    "name": {
      "title": "Name",
      "description": "Identifying the purpose and intended use of the property, part or other object.",
      "type": "string"
    },
    "id": {
      "title": "Identifier",
      "description": "Unique identifier of the containing object",
      "type": "string"
    },
    "ns": {
      "title": "Namespace",
      "description": "A namespace qualifying the name.",
      "type": "string"
    },
    "class": {
      "title": "Class",
      "description": "Indicating the type or classification of the containing object",
      "type": "string"
    },
    "value": {
      "type": "string"
    }
  },
  "required": [
    "value",
    "name"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-results-prose'>**Prose**</a>: Prose permits multiple paragraphs, lists, tables etc.
```json
{
  "title": "Prose",
  "description": "Prose permits multiple paragraphs, lists, tables etc.",
  "$id": "#/definitions/prose",
  "type": "string"
}
```
- <a id='assessment-results-protocol'>**Protocol**</a>: Information about the protocol used to provide a service.
```json
{
  "title": "Protocol",
  "description": "Information about the protocol used to provide a service.",
  "$id": "#/definitions/protocol",
  "type": "object",
  "properties": {
    "uuid": {
      "title": "Universally Unique Identifier",
      "description": "A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "name": {
      "description": "The short name of the protocol (e.g., TLS).",
      "type": "string"
    },
    "title": {
      "$ref": "#/definitions/title"
    },
    "port-ranges": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/port-range"
      }
    }
  },
  "required": [
    "name"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-results-publication_timestamp'>**Publication Timestamp**</a>: The date and time this document was published.
```json
{
  "title": "Publication Timestamp",
  "description": "The date and time this document was published.",
  "$id": "#/definitions/published",
  "type": "string",
  "format": "date-time",
  "pattern": "^((2000|2400|2800|(19|2[0-9](0[48]|[2468][048]|[13579][26])))-02-29)|(((19|2[0-9])[0-9]{2})-02-(0[1-9]|1[0-9]|2[0-8]))|(((19|2[0-9])[0-9]{2})-(0[13578]|10|12)-(0[1-9]|[12][0-9]|3[01]))|(((19|2[0-9])[0-9]{2})-(0[469]|11)-(0[1-9]|[12][0-9]|30))T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\\.[0-9]+)?(Z|[+-][0-9]{2}:[0-9]{2})$"
}
```
- <a id='assessment-results-purpose'>**Purpose**</a>: Describes the purpose for the service within the system.
```json
{
  "title": "Purpose",
  "description": "Describes the purpose for the service within the system.",
  "$id": "#/definitions/purpose",
  "type": "string"
}
```
- <a id='assessment-results-relevant_evidence'>**Relevant Evidence**</a>: Links this observation to relevant evidence.
```json
{
  "title": "Relevant Evidence",
  "description": "Links this observation to relevant evidence.",
  "$id": "#/definitions/relevant-evidence",
  "type": "object",
  "properties": {
    "href": {
      "description": "Links to evidence as URI. May use a URI fragment to point to a resource in the back-matter.",
      "type": "string",
      "format": "uri-reference"
    },
    "description": {
      "$ref": "#/definitions/description"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "description"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-results-remarks'>**Remarks**</a>: Additional commentary on the parent item.
```json
{
  "title": "Remarks",
  "description": "Additional commentary on the parent item.",
  "$id": "#/definitions/remarks",
  "type": "string"
}
```
- <a id='assessment-results-remediation'>**Remediation**</a>: Describes either recommendation or an actual plan for remediating the risk.
```json
{
  "title": "Remediation",
  "description": "Describes either recommendation or an actual plan for remediating the risk.",
  "$id": "#/definitions/remediation",
  "type": "object",
  "properties": {
    "uuid": {
      "title": "Universally Unique Identifier",
      "description": "A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "type": {
      "title": "Type",
      "description": "Indicating the type of identifier, address, email or other data item.",
      "type": "string"
    },
    "title": {
      "$ref": "#/definitions/title"
    },
    "description": {
      "$ref": "#/definitions/description"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "origins": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/remediation-origin"
      }
    },
    "requirements": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/required"
      }
    },
    "schedule": {
      "$ref": "#/definitions/schedule"
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "uuid",
    "title",
    "description"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-results-remediation_origin'>**Remediation Origin**</a>: Points to the source of the remediation recommendation or plan
```json
{
  "title": "Remediation Origin",
  "description": "Points to the source of the remediation recommendation or plan",
  "$id": "#/definitions/remediation-origin",
  "type": "object",
  "properties": {
    "uuid-ref": {
      "title": "UUID Reference",
      "description": "A pointer to a relevant item, using it's UUID.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "type": {
      "title": "Type",
      "description": "Indicating the type of identifier, address, email or other data item.",
      "type": "string"
    },
    "STRVALUE": {
      "type": "string"
    }
  },
  "required": [
    "STRVALUE",
    "uuid-ref"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-results-remediation_tracking'>**Remediation Tracking**</a>: A log of events and actions taken towards the remediation of the associated risk.
```json
{
  "title": "Remediation Tracking",
  "description": "A log of events and actions taken towards the remediation of the associated risk.",
  "$id": "#/definitions/remediation-tracking",
  "type": "object",
  "properties": {
    "tracking-entries": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/tracking-entry"
      }
    }
  },
  "required": [
    "tracking-entries"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-results-required'>**Required**</a>: Identifies something required to achieve remediation.
```json
{
  "title": "Required",
  "description": "Identifies something required to achieve remediation.",
  "$id": "#/definitions/required",
  "type": "object",
  "properties": {
    "uuid": {
      "title": "Universally Unique Identifier",
      "description": "A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "subject-references": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/subject-reference"
      }
    },
    "title": {
      "$ref": "#/definitions/title"
    },
    "description": {
      "$ref": "#/definitions/description"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "uuid",
    "description"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-results-resource'>**Resource**</a>: A resource associated with the present document, which may be a pointer to other data or a citation.
```json
{
  "title": "Resource",
  "description": "A resource associated with the present document, which may be a pointer to other data or a citation.",
  "$id": "#/definitions/resource",
  "type": "object",
  "properties": {
    "uuid": {
      "title": "Universally Unique Identifier",
      "description": "A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "title": {
      "$ref": "#/definitions/title"
    },
    "desc": {
      "$ref": "#/definitions/desc"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "document-ids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/doc-id"
      }
    },
    "citation": {
      "$ref": "#/definitions/citation"
    },
    "rlinks": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/rlink"
      }
    },
    "attachments": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/base64"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "uuid"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-results-responsible_party'>**Responsible Party**</a>: A reference to a set of organizations or persons that have responsibility for performing a referenced role relative to the parent context.
```json
{
  "title": "Responsible Party",
  "description": "A reference to a set of organizations or persons that have responsibility for performing a referenced role relative to the parent context.",
  "$id": "#/definitions/responsible-party",
  "type": "object",
  "properties": {
    "party-uuids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/party-uuid"
      }
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "party-uuids"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-results-responsible_role'>**Responsible Role**</a>: A reference to one or more roles with responsibility for performing a function relative to the control.
```json
{
  "title": "Responsible Role",
  "description": "A reference to one or more roles with responsibility for performing a function relative to the control.",
  "$id": "#/definitions/responsible-role",
  "type": "object",
  "properties": {
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "party-ids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/party-uuid"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "additionalProperties": false
}
```
- <a id='assessment-results-result'>**Result**</a>: A brief indication as to whether the objective is satisfied or not.
```json
{
  "title": "Result",
  "description": "A brief indication as to whether the objective is satisfied or not.",
  "$id": "#/definitions/result",
  "type": "object",
  "properties": {
    "system": {
      "title": "Assessment System",
      "description": "Identifies the framework or rules to which this value conforms.",
      "type": "string",
      "format": "uri"
    },
    "STRVALUE": {
      "type": "string"
    }
  },
  "required": [
    "STRVALUE"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-results-assessment_results'>**Assessment Results**</a>: Used by the assessment results and POA&M. In the assessment results, this identifies all of the assessment observations and findings, initial and residual risks, deviations, and disposition. In the POA&M, this identifies initial and residual risks, deviations, and disposition.
```json
{
  "title": "Assessment Results",
  "description": "Used by the assessment results and POA&M. In the assessment results, this identifies all of the assessment observations and findings, initial and residual risks, deviations, and disposition. In the POA&M, this identifies initial and residual risks, deviations, and disposition.",
  "$id": "#/definitions/results",
  "type": "object",
  "properties": {
    "uuid": {
      "title": "Universally Unique Identifier",
      "description": "A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "title": {
      "$ref": "#/definitions/title"
    },
    "description": {
      "$ref": "#/definitions/description"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "start": {
      "$ref": "#/definitions/start"
    },
    "end": {
      "$ref": "#/definitions/end"
    },
    "findings": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/finding"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "uuid",
    "title",
    "description",
    "start",
    "end",
    "findings"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-results-revision_history_entry'>**Revision History Entry**</a>: An entry in a sequential list of revisions to the containing document in reverse chronological order (i.e., most recent previous revision first).
```json
{
  "title": "Revision History Entry",
  "description": "An entry in a sequential list of revisions to the containing document in reverse chronological order (i.e., most recent previous revision first).",
  "$id": "#/definitions/revision",
  "type": "object",
  "properties": {
    "title": {
      "$ref": "#/definitions/title"
    },
    "published": {
      "$ref": "#/definitions/published"
    },
    "last-modified": {
      "$ref": "#/definitions/last-modified"
    },
    "version": {
      "$ref": "#/definitions/version"
    },
    "oscal-version": {
      "$ref": "#/definitions/oscal-version"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "additionalProperties": false
}
```
- <a id='assessment-results-identified_risk'>**Identified Risk**</a>: An identified risk.
```json
{
  "title": "Identified Risk",
  "description": "An identified risk.",
  "$id": "#/definitions/risk",
  "type": "object",
  "properties": {
    "uuid": {
      "title": "Universally Unique Identifier",
      "description": "A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "title": {
      "$ref": "#/definitions/title"
    },
    "description": {
      "$ref": "#/definitions/description"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "risk-metrics": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/risk-metric"
      }
    },
    "risk-statement": {
      "$ref": "#/definitions/risk-statement"
    },
    "mitigating-factors": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/mitigating-factor"
      }
    },
    "remediation-group": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/remediation"
      }
    },
    "risk-status": {
      "$ref": "#/definitions/risk-status"
    },
    "closure-actions": {
      "$ref": "#/definitions/closure-actions"
    },
    "remediation-tracking": {
      "$ref": "#/definitions/remediation-tracking"
    },
    "party-uuids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/party-uuid"
      }
    }
  },
  "required": [
    "uuid",
    "title",
    "description",
    "risk-statement",
    "risk-status"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-results-risk_metric'>**Risk Metric**</a>: An individual risk metric from a specified system.
```json
{
  "title": "Risk Metric",
  "description": "An individual risk metric from a specified system.",
  "$id": "#/definitions/risk-metric",
  "type": "object",
  "properties": {
    "name": {
      "title": "Name",
      "description": "Identifying the purpose and intended use of the property, part or other object.",
      "type": "string"
    },
    "class": {
      "title": "Class",
      "description": "Indicating the type or classification of the containing object",
      "type": "string"
    },
    "system": {
      "title": "System",
      "description": "Specifies the system represented by this risk metric.",
      "type": "string"
    },
    "STRVALUE": {
      "type": "string"
    }
  },
  "required": [
    "STRVALUE",
    "name"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-results-risk_statement'>**Risk Statement**</a>: Describes the risk.
```json
{
  "title": "Risk Statement",
  "description": "Describes the risk.",
  "$id": "#/definitions/risk-statement",
  "type": "string"
}
```
- <a id='assessment-results-status'>**Status**</a>: Describes the status of the associated risk.
```json
{
  "title": "Status",
  "description": "Describes the status of the associated risk.",
  "$id": "#/definitions/risk-status",
  "type": "string"
}
```
- <a id='assessment-results-resource_link'>**Resource link**</a>: A pointer to an external copy of a document with optional hash for verification
```json
{
  "title": "Resource link",
  "description": "A pointer to an external copy of a document with optional hash for verification",
  "$id": "#/definitions/rlink",
  "type": "object",
  "properties": {
    "href": {
      "title": "hypertext reference",
      "description": "A link to a document or document fragment (actual, nominal or projected)",
      "type": "string",
      "format": "uri-reference"
    },
    "media-type": {
      "title": "Media type",
      "description": "Describes the media type of the linked resource",
      "type": "string"
    },
    "hashes": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/hash"
      }
    }
  },
  "required": [
    "href"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-results-role'>**Role**</a>: Defining a role to be assigned to a party
```json
{
  "title": "Role",
  "description": "Defining a role to be assigned to a party",
  "$id": "#/definitions/role",
  "type": "object",
  "properties": {
    "id": {
      "title": "Identifier",
      "description": "Unique identifier of the containing object",
      "type": "string"
    },
    "title": {
      "$ref": "#/definitions/title"
    },
    "short-name": {
      "$ref": "#/definitions/short-name"
    },
    "desc": {
      "$ref": "#/definitions/desc"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "id",
    "title"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-results-role_identifier_reference'>**Role Identifier Reference**</a>: A reference to the roles served by the user.
```json
{
  "title": "Role Identifier Reference",
  "description": "A reference to the roles served by the user.",
  "$id": "#/definitions/role-id",
  "type": "string"
}
```
- <a id='assessment-results-schedule'>**Schedule**</a>: Identifies the schedule for the assessment activities.
```json
{
  "title": "Schedule",
  "description": "Identifies the schedule for the assessment activities.",
  "$id": "#/definitions/schedule",
  "type": "object",
  "properties": {
    "uuid": {
      "title": "Universally Unique Identifier",
      "description": "A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "tasks": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/task"
      }
    }
  },
  "required": [
    "tasks"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-results-sequence_number'>**Sequence Number**</a>: Identifies the sequence number for the test step.
```json
{
  "title": "Sequence Number",
  "description": "Identifies the sequence number for the test step.",
  "$id": "#/definitions/sequence",
  "type": "integer"
}
```
- <a id='assessment-results-short-name'>**short-name**</a>: A common name, short name or acronym
```json
{
  "title": "short-name",
  "description": "A common name, short name or acronym",
  "$id": "#/definitions/short-name",
  "type": "string"
}
```
- <a id='assessment-results-start'>**Start**</a>: Identifies the start of a task.
```json
{
  "title": "Start",
  "description": "Identifies the start of a task.",
  "$id": "#/definitions/start",
  "type": "string",
  "format": "date-time",
  "pattern": "^((2000|2400|2800|(19|2[0-9](0[48]|[2468][048]|[13579][26])))-02-29)|(((19|2[0-9])[0-9]{2})-02-(0[1-9]|1[0-9]|2[0-8]))|(((19|2[0-9])[0-9]{2})-(0[13578]|10|12)-(0[1-9]|[12][0-9]|3[01]))|(((19|2[0-9])[0-9]{2})-(0[469]|11)-(0[1-9]|[12][0-9]|30))T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\\.[0-9]+)?(Z|[+-][0-9]{2}:[0-9]{2})$"
}
```
- <a id='assessment-results-state'>**State**</a>: State, province or analogous geographical region for mailing address
```json
{
  "title": "State",
  "description": "State, province or analogous geographical region for mailing address",
  "$id": "#/definitions/state",
  "type": "string"
}
```
- <a id='assessment-results-status'>**Status**</a>: Describes the operational status of the system.
```json
{
  "title": "Status",
  "description": "Describes the operational status of the system.",
  "$id": "#/definitions/status",
  "type": "object",
  "properties": {
    "state": {
      "title": "State",
      "description": "The current operating status.",
      "type": "string",
      "enum": [
        "operational",
        "under-development",
        "under-major-modification",
        "disposition",
        "other"
      ]
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "state"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-results-identifies_the_subject'>**Identifies the Subject**</a>: A pointer to a resource based on its ID. Use type to indicate whether the identified resource is a component, inventory item, location, user, or something else.
```json
{
  "title": "Identifies the Subject",
  "description": "A pointer to a resource based on its ID. Use type to indicate whether the identified resource is a component, inventory item, location, user, or something else.",
  "$id": "#/definitions/subject-reference",
  "type": "object",
  "properties": {
    "uuid-ref": {
      "title": "UUID Reference",
      "description": "A pointer to a component, inventory-item, location, party, user, or resource using it's UUID.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "type": {
      "title": "Type",
      "description": "Indicating the type of identifier, address, email or other data item.",
      "type": "string"
    },
    "title": {
      "$ref": "#/definitions/title"
    },
    "props": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    }
  },
  "required": [
    "uuid-ref",
    "type"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-results-task'>**Task**</a>: Identifies an individual task.
```json
{
  "title": "Task",
  "description": "Identifies an individual task.",
  "$id": "#/definitions/task",
  "type": "object",
  "properties": {
    "uuid": {
      "title": "Universally Unique Identifier",
      "description": "A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "title": {
      "$ref": "#/definitions/title"
    },
    "description": {
      "$ref": "#/definitions/description"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "start": {
      "$ref": "#/definitions/start"
    },
    "end": {
      "$ref": "#/definitions/end"
    },
    "activity-uuids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/activity-uuid"
      }
    },
    "role-ids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/role-id"
      }
    },
    "party-uuids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/party-uuid"
      }
    },
    "location-uuids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/location-uuid"
      }
    },
    "compare-to": {
      "$ref": "#/definitions/compare-to"
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "uuid"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-results-test_method'>**Test Method**</a>: Identifies an individual test method.
```json
{
  "title": "Test Method",
  "description": "Identifies an individual test method.",
  "$id": "#/definitions/test-method",
  "type": "object",
  "properties": {
    "uuid": {
      "title": "Universally Unique Identifier",
      "description": "A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "title": {
      "$ref": "#/definitions/title"
    },
    "description": {
      "$ref": "#/definitions/description"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "test-steps": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/test-step"
      }
    },
    "compare-to": {
      "$ref": "#/definitions/compare-to"
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "uuid"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-results-test_steps'>**Test Steps**</a>: Identifies an individual test step.
```json
{
  "title": "Test Steps",
  "description": "Identifies an individual test step.",
  "$id": "#/definitions/test-step",
  "type": "object",
  "properties": {
    "uuid": {
      "title": "Universally Unique Identifier",
      "description": "A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "sequence": {
      "$ref": "#/definitions/sequence"
    },
    "description": {
      "$ref": "#/definitions/description"
    },
    "role-ids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/role-id"
      }
    },
    "party-uuids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/party-uuid"
      }
    },
    "compare-to": {
      "$ref": "#/definitions/compare-to"
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "uuid",
    "description"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-results-text'>**Text**</a>: A line of textual content whose semantic is determined by the context of use.
```json
{
  "title": "Text",
  "description": "A line of textual content whose semantic is determined by the context of use.",
  "$id": "#/definitions/text",
  "type": "string"
}
```
- <a id='assessment-results-threat_id'>**Threat ID**</a>: A pointer, by ID, to an externally-defined threat.
```json
{
  "title": "Threat ID",
  "description": "A pointer, by ID, to an externally-defined threat.",
  "$id": "#/definitions/threat-id",
  "type": "object",
  "properties": {
    "system": {
      "title": "Threat Type Identification System",
      "description": "Specifies the source of the threat information.",
      "type": "string",
      "format": "uri"
    },
    "uri": {
      "title": "URI",
      "description": "An optional location for the threat data, from which this ID originates.",
      "type": "string",
      "format": "uri"
    },
    "STRVALUE": {
      "type": "string"
    }
  },
  "required": [
    "STRVALUE",
    "system"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-results-title'>**Title**</a>: A title for display and navigation
```json
{
  "title": "Title",
  "description": "A title for display and navigation",
  "$id": "#/definitions/title",
  "type": "string"
}
```
- <a id='assessment-results-assessment_assets'>**Assessment Assets**</a>: The technology tools used by the assessor to perform the assessment, such as vulnerability scanners. In the assessment plan these are the intended tools. In the assessment results, these are the actual tools used, including any differences from the assessment plan.
```json
{
  "title": "Assessment Assets",
  "description": "The technology tools used by the assessor to perform the assessment, such as vulnerability scanners. In the assessment plan these are the intended tools. In the assessment results, these are the actual tools used, including any differences from the assessment plan.",
  "$id": "#/definitions/tools",
  "type": "object",
  "properties": {
    "components": {
      "type": "object",
      "minProperties": 1,
      "additionalProperties": {
        "allOf": [
          {
            "type": "object",
            "$ref": "#/definitions/component"
          },
          {
            "not": {
              "type": "string"
            }
          }
        ]
      }
    }
  },
  "additionalProperties": false
}
```
- <a id='assessment-results-tracking_entry'>**Tracking Entry**</a>: Individual remediation tracking entry, which logs an event or action taken towards the remediation of the associated risk.
```json
{
  "title": "Tracking Entry",
  "description": "Individual remediation tracking entry, which logs an event or action taken towards the remediation of the associated risk.",
  "$id": "#/definitions/tracking-entry",
  "type": "object",
  "properties": {
    "uuid": {
      "title": "Universally Unique Identifier",
      "description": "A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "type": {
      "title": "Type",
      "description": "Indicating the type of identifier, address, email or other data item.",
      "type": "string"
    },
    "date-time-stamp": {
      "$ref": "#/definitions/date-time-stamp"
    },
    "title": {
      "$ref": "#/definitions/title"
    },
    "description": {
      "$ref": "#/definitions/description"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "uuid",
    "date-time-stamp",
    "description"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-results-url'>**URL**</a>: URL for web site or Internet presence
```json
{
  "title": "URL",
  "description": "URL for web site or Internet presence",
  "$id": "#/definitions/url",
  "type": "string",
  "format": "uri"
}
```
- <a id='assessment-results-system_user_class'>**System User Class**</a>: A type of user that interacts with the system based on an associated role.
```json
{
  "title": "System User Class",
  "description": "A type of user that interacts with the system based on an associated role.",
  "$id": "#/definitions/user",
  "type": "object",
  "properties": {
    "title": {
      "$ref": "#/definitions/title"
    },
    "short-name": {
      "$ref": "#/definitions/short-name"
    },
    "description": {
      "$ref": "#/definitions/description"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "role-ids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/role-id"
      }
    },
    "authorized-privileges": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/authorized-privilege"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "role-ids"
  ],
  "additionalProperties": false
}
```
- <a id='assessment-results-document_version'>**Document version**</a>: The version of the document content.
```json
{
  "title": "Document version",
  "description": "The version of the document content.",
  "$id": "#/definitions/version",
  "type": "string"
}
```

## catalog

> OSCAL Control Catalog Format

- <a id='catalog-address_line'>**Address line**</a>: A single line of an address.
```json
{
  "title": "Address line",
  "description": "A single line of an address.",
  "$id": "#/definitions/addr-line",
  "type": "string"
}
```
- <a id='catalog-address'>**Address**</a>: A postal address.
```json
{
  "title": "Address",
  "description": "A postal address.",
  "$id": "#/definitions/address",
  "type": "object",
  "properties": {
    "type": {
      "description": "Indicates the type of address.",
      "type": "string"
    },
    "postal-address": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/addr-line"
      }
    },
    "city": {
      "$ref": "#/definitions/city"
    },
    "state": {
      "$ref": "#/definitions/state"
    },
    "postal-code": {
      "$ref": "#/definitions/postal-code"
    },
    "country": {
      "$ref": "#/definitions/country"
    }
  },
  "additionalProperties": false
}
```
- <a id='catalog-annotation'>**Annotation**</a>: A name/value pair with optional explanatory remarks.
```json
{
  "title": "Annotation",
  "description": "A name/value pair with optional explanatory remarks.",
  "$id": "#/definitions/annotation",
  "type": "object",
  "properties": {
    "name": {
      "title": "Name",
      "description": "Identifying the purpose and intended use of the property, part or other object.",
      "type": "string"
    },
    "id": {
      "title": "Identifier",
      "description": "Unique identifier of the containing object",
      "type": "string"
    },
    "ns": {
      "title": "Namespace",
      "description": "A namespace qualifying the name.",
      "type": "string"
    },
    "value": {
      "title": "Value",
      "description": "Indicates the value of the characteristic.",
      "type": "string"
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "name"
  ],
  "additionalProperties": false
}
```
- <a id='catalog-back_matter'>**Back matter**</a>: A collection of citations and resource references.
```json
{
  "title": "Back matter",
  "description": "A collection of citations and resource references.",
  "$id": "#/definitions/back-matter",
  "type": "object",
  "properties": {
    "resources": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/resource"
      }
    }
  },
  "additionalProperties": false
}
```
- <a id='catalog-base64'>**Base64**</a>: 
```json
{
  "title": "Base64",
  "description": "",
  "$id": "#/definitions/base64",
  "type": "object",
  "properties": {
    "filename": {
      "title": "File Name",
      "description": "Name of the file before it was encoded as Base64 to be embedded in a resource. This is the name that will be assigned to the file when the file is decoded.",
      "type": "string",
      "format": "uri-reference"
    },
    "media-type": {
      "title": "Media type",
      "description": "Describes the media type of the linked resource",
      "type": "string"
    },
    "value": {
      "type": "string"
    }
  },
  "required": [
    "value"
  ],
  "additionalProperties": false
}
```
- <a id='catalog-bibliographic_definition'>**Bibliographic Definition**</a>: A container in which a set of bibliographic information can included. The model of this information is undefined by OSCAL.
```json
{
  "title": "Bibliographic Definition",
  "description": "A container in which a set of bibliographic information can included. The model of this information is undefined by OSCAL.",
  "$id": "#/definitions/biblio",
  "type": "object",
  "additionalProperties": false
}
```
- <a id='catalog-catalog'>**Catalog**</a>: A collection of controls.
```json
{
  "title": "Catalog",
  "description": "A collection of controls.",
  "$id": "#/definitions/catalog",
  "type": "object",
  "properties": {
    "uuid": {
      "title": "Universally Unique Identifier",
      "description": "A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "metadata": {
      "$ref": "#/definitions/metadata"
    },
    "parameters": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/param"
      }
    },
    "controls": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/control"
      }
    },
    "groups": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/group"
      }
    },
    "back-matter": {
      "$ref": "#/definitions/back-matter"
    }
  },
  "required": [
    "uuid",
    "metadata"
  ],
  "additionalProperties": false
}
```
- <a id='catalog-choice'>**Choice**</a>: A value selection among several such options
```json
{
  "title": "Choice",
  "description": "A value selection among several such options",
  "$id": "#/definitions/choice",
  "type": "string"
}
```
- <a id='catalog-citation'>**Citation**</a>: A citation consisting of end note text and optional structured bibliographic data.
```json
{
  "title": "Citation",
  "description": "A citation consisting of end note text and optional structured bibliographic data.",
  "$id": "#/definitions/citation",
  "type": "object",
  "properties": {
    "text": {
      "$ref": "#/definitions/text"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "biblio": {
      "$ref": "#/definitions/biblio"
    }
  },
  "required": [
    "text"
  ],
  "additionalProperties": false
}
```
- <a id='catalog-city'>**City**</a>: City, town or geographical region for mailing address
```json
{
  "title": "City",
  "description": "City, town or geographical region for mailing address",
  "$id": "#/definitions/city",
  "type": "string"
}
```
- <a id='catalog-constraint'>**Constraint**</a>: A formal or informal expression of a constraint or test
```json
{
  "title": "Constraint",
  "description": "A formal or informal expression of a constraint or test",
  "$id": "#/definitions/constraint",
  "type": "object",
  "properties": {
    "test": {
      "title": "Constraint test",
      "description": "A formal (executable) expression of a constraint",
      "type": "string"
    },
    "detail": {
      "type": "string"
    }
  },
  "required": [
    "detail"
  ],
  "additionalProperties": false
}
```
- <a id='catalog-control'>**Control**</a>: A structured information object representing a security or privacy control. Each security or privacy control within the Catalog is defined by a distinct control instance.
```json
{
  "title": "Control",
  "description": "A structured information object representing a security or privacy control. Each security or privacy control within the Catalog is defined by a distinct control instance.",
  "$id": "#/definitions/control",
  "type": "object",
  "properties": {
    "id": {
      "title": "Identifier",
      "description": "Unique identifier of the containing object",
      "type": "string"
    },
    "class": {
      "title": "Class",
      "description": "Indicating the type or classification of the containing object",
      "type": "string"
    },
    "title": {
      "$ref": "#/definitions/title"
    },
    "parameters": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/param"
      }
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "parts": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/part"
      }
    },
    "controls": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/control"
      }
    }
  },
  "required": [
    "id",
    "title"
  ],
  "additionalProperties": false
}
```
- <a id='catalog-country'>**Country**</a>: Country for mailing address
```json
{
  "title": "Country",
  "description": "Country for mailing address",
  "$id": "#/definitions/country",
  "type": "string"
}
```
- <a id='catalog-description'>**Description**</a>: A short textual description
```json
{
  "title": "Description",
  "description": "A short textual description",
  "$id": "#/definitions/desc",
  "type": "string"
}
```
- <a id='catalog-document_identifier'>**Document Identifier**</a>: A document identifier qualified by an identifier type.
```json
{
  "title": "Document Identifier",
  "description": "A document identifier qualified by an identifier type.",
  "$id": "#/definitions/doc-id",
  "type": "object",
  "properties": {
    "type": {
      "description": "Qualifies the kind of document identifier.",
      "type": "string"
    },
    "identifier": {
      "type": "string"
    }
  },
  "required": [
    "identifier",
    "type"
  ],
  "additionalProperties": false
}
```
- <a id='catalog-email'>**Email**</a>: Email address
```json
{
  "title": "Email",
  "description": "Email address",
  "$id": "#/definitions/email",
  "type": "string",
  "format": "email",
  "pattern": "^.+@.+"
}
```
- <a id='catalog-personal_identifier'>**Personal Identifier**</a>: An identifier for a person (such as an ORCID) using a designated scheme.
```json
{
  "title": "Personal Identifier",
  "description": "An identifier for a person (such as an ORCID) using a designated scheme.",
  "$id": "#/definitions/external-id",
  "type": "object",
  "properties": {
    "type": {
      "title": "Type",
      "description": "Indicating the type of identifier, address, email or other data item.",
      "type": "string"
    },
    "id": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "type"
  ],
  "additionalProperties": false
}
```
- <a id='catalog-control_group'>**Control Group**</a>: A group of controls, or of groups of controls.
```json
{
  "title": "Control Group",
  "description": "A group of controls, or of groups of controls.",
  "$id": "#/definitions/group",
  "type": "object",
  "properties": {
    "id": {
      "title": "Identifier",
      "description": "Unique identifier of the containing object",
      "type": "string"
    },
    "class": {
      "title": "Class",
      "description": "Indicating the type or classification of the containing object",
      "type": "string"
    },
    "title": {
      "$ref": "#/definitions/title"
    },
    "parameters": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/param"
      }
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "parts": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/part"
      }
    },
    "groups": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/group"
      }
    },
    "controls": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/control"
      }
    }
  },
  "required": [
    "title"
  ],
  "additionalProperties": false
}
```
- <a id='catalog-guideline'>**Guideline**</a>: A prose statement that provides a recommendation for the use of a parameter.
```json
{
  "title": "Guideline",
  "description": "A prose statement that provides a recommendation for the use of a parameter.",
  "$id": "#/definitions/guideline",
  "type": "object",
  "properties": {
    "prose": {
      "$ref": "#/definitions/prose"
    }
  },
  "additionalProperties": false
}
```
- <a id='catalog-hash'>**Hash**</a>: A representation of a cryptographic digest generated over a resource using a hash algorithm.
```json
{
  "title": "Hash",
  "description": "A representation of a cryptographic digest generated over a resource using a hash algorithm.",
  "$id": "#/definitions/hash",
  "type": "object",
  "properties": {
    "algorithm": {
      "title": "Hash algorithm",
      "description": "Method by which a hash is derived",
      "type": "string"
    },
    "value": {
      "type": "string"
    }
  },
  "required": [
    "value",
    "algorithm"
  ],
  "additionalProperties": false
}
```
- <a id='catalog-parameter_label'>**Parameter label**</a>: A placeholder for a missing value, in display.
```json
{
  "title": "Parameter label",
  "description": "A placeholder for a missing value, in display.",
  "$id": "#/definitions/label",
  "type": "string"
}
```
- <a id='catalog-last_modified_timestamp'>**Last modified timestamp**</a>: Date and time of last modification.
```json
{
  "title": "Last modified timestamp",
  "description": "Date and time of last modification.",
  "$id": "#/definitions/last-modified",
  "type": "string",
  "format": "date-time",
  "pattern": "^((2000|2400|2800|(19|2[0-9](0[48]|[2468][048]|[13579][26])))-02-29)|(((19|2[0-9])[0-9]{2})-02-(0[1-9]|1[0-9]|2[0-8]))|(((19|2[0-9])[0-9]{2})-(0[13578]|10|12)-(0[1-9]|[12][0-9]|3[01]))|(((19|2[0-9])[0-9]{2})-(0[469]|11)-(0[1-9]|[12][0-9]|30))T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\\.[0-9]+)?(Z|[+-][0-9]{2}:[0-9]{2})$"
}
```
- <a id='catalog-link'>**Link**</a>: A reference to a local or remote resource
```json
{
  "title": "Link",
  "description": "A reference to a local or remote resource",
  "$id": "#/definitions/link",
  "type": "object",
  "properties": {
    "href": {
      "title": "hypertext reference",
      "description": "A link to a document or document fragment (actual, nominal or projected)",
      "type": "string",
      "format": "uri-reference"
    },
    "rel": {
      "title": "Relation",
      "description": "Describes the type of relationship provided by the link. This can be an indicator of the link's purpose.",
      "type": "string"
    },
    "media-type": {
      "title": "Media type",
      "description": "Describes the media type of the linked resource",
      "type": "string"
    },
    "text": {
      "type": "string"
    }
  },
  "required": [
    "text",
    "href"
  ],
  "additionalProperties": false
}
```
- <a id='catalog-location'>**Location**</a>: A location, with associated metadata that can be referenced.
```json
{
  "title": "Location",
  "description": "A location, with associated metadata that can be referenced.",
  "$id": "#/definitions/location",
  "type": "object",
  "properties": {
    "uuid": {
      "title": "Universally Unique Identifier",
      "description": "A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "title": {
      "$ref": "#/definitions/title"
    },
    "address": {
      "$ref": "#/definitions/address"
    },
    "email-addresses": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/email"
      }
    },
    "telephone-numbers": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/phone"
      }
    },
    "URLs": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/url"
      }
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "uuid",
    "address"
  ],
  "additionalProperties": false
}
```
- <a id='catalog-location_reference'>**Location Reference**</a>: References a location defined in metadata.
```json
{
  "title": "Location Reference",
  "description": "References a location defined in metadata.",
  "$id": "#/definitions/location-uuid",
  "type": "string",
  "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
}
```
- <a id='catalog-organizational_affiliation'>**Organizational Affiliation**</a>: Identifies that the containing object is a member of the organization associated with the provided UUID.
```json
{
  "title": "Organizational Affiliation",
  "description": "Identifies that the containing object is a member of the organization associated with the provided UUID.",
  "$id": "#/definitions/member-of-organization",
  "type": "string",
  "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
}
```
- <a id='catalog-publication_metadata'>**Publication metadata**</a>: Provides information about the publication and availability of the containing document.
```json
{
  "title": "Publication metadata",
  "description": "Provides information about the publication and availability of the containing document.",
  "$id": "#/definitions/metadata",
  "type": "object",
  "properties": {
    "title": {
      "$ref": "#/definitions/title"
    },
    "published": {
      "$ref": "#/definitions/published"
    },
    "last-modified": {
      "$ref": "#/definitions/last-modified"
    },
    "version": {
      "$ref": "#/definitions/version"
    },
    "oscal-version": {
      "$ref": "#/definitions/oscal-version"
    },
    "revision-history": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/revision"
      }
    },
    "document-ids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/doc-id"
      }
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "roles": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/role"
      }
    },
    "locations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/location"
      }
    },
    "parties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/party"
      }
    },
    "responsible-parties": {
      "type": "object",
      "minProperties": 1,
      "additionalProperties": {
        "allOf": [
          {
            "type": "object",
            "$ref": "#/definitions/responsible-party"
          },
          {
            "not": {
              "type": "string"
            }
          }
        ]
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "title",
    "last-modified",
    "version",
    "oscal-version"
  ],
  "additionalProperties": false
}
```
- <a id='catalog-oscal_version'>**OSCAL version**</a>: OSCAL model version.
```json
{
  "title": "OSCAL version",
  "description": "OSCAL model version.",
  "$id": "#/definitions/oscal-version",
  "type": "string"
}
```
- <a id='catalog-parameter'>**Parameter**</a>: Parameters provide a mechanism for the dynamic assignment of value(s) in a control.
```json
{
  "title": "Parameter",
  "description": "Parameters provide a mechanism for the dynamic assignment of value(s) in a control.",
  "$id": "#/definitions/param",
  "type": "object",
  "properties": {
    "id": {
      "title": "Identifier",
      "description": "Unique identifier of the containing object",
      "type": "string"
    },
    "class": {
      "title": "Class",
      "description": "Indicating the type or classification of the containing object",
      "type": "string"
    },
    "depends-on": {
      "title": "Depends on",
      "description": "Another parameter invoking this one",
      "type": "string"
    },
    "label": {
      "$ref": "#/definitions/label"
    },
    "descriptions": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/usage"
      }
    },
    "constraints": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/constraint"
      }
    },
    "guidance": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/guideline"
      }
    },
    "value": {
      "$ref": "#/definitions/value"
    },
    "select": {
      "$ref": "#/definitions/select"
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    }
  },
  "required": [
    "id"
  ],
  "additionalProperties": false
}
```
- <a id='catalog-part'>**Part**</a>: A partition or component of a control or part
```json
{
  "title": "Part",
  "description": "A partition or component of a control or part",
  "$id": "#/definitions/part",
  "type": "object",
  "properties": {
    "id": {
      "title": "Identifier",
      "description": "Unique identifier of the containing object",
      "type": "string"
    },
    "name": {
      "title": "Name",
      "description": "Identifying the purpose and intended use of the property, part or other object.",
      "type": "string"
    },
    "ns": {
      "title": "Namespace",
      "description": "A namespace qualifying the name.",
      "type": "string"
    },
    "class": {
      "title": "Class",
      "description": "Indicating the type or classification of the containing object",
      "type": "string"
    },
    "title": {
      "$ref": "#/definitions/title"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "prose": {
      "$ref": "#/definitions/prose"
    },
    "parts": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/part"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    }
  },
  "required": [
    "name"
  ],
  "additionalProperties": false
}
```
- <a id='catalog-party_(organization_or_person)'>**Party (organization or person)**</a>: A responsible entity, either singular (an organization or person) or collective (multiple persons)
```json
{
  "title": "Party (organization or person)",
  "description": "A responsible entity, either singular (an organization or person) or collective (multiple persons)",
  "$id": "#/definitions/party",
  "type": "object",
  "properties": {
    "uuid": {
      "title": "Universally Unique Identifier",
      "description": "A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "type": {
      "title": "Party Type",
      "description": "A category describing the kind of party the object describes.",
      "type": "string",
      "enum": [
        "person",
        "organization"
      ]
    },
    "party-name": {
      "$ref": "#/definitions/party-name"
    },
    "short-name": {
      "$ref": "#/definitions/short-name"
    },
    "external-ids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/external-id"
      }
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "addresses": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/address"
      }
    },
    "email-addresses": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/email"
      }
    },
    "telephone-numbers": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/phone"
      }
    },
    "member-of-organizations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/member-of-organization"
      }
    },
    "location-uuids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/location-uuid"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "uuid",
    "type",
    "party-name"
  ],
  "additionalProperties": false
}
```
- <a id='catalog-party_name'>**Party Name**</a>: The full (legal) name of the party.
```json
{
  "title": "Party Name",
  "description": "The full (legal) name of the party.",
  "$id": "#/definitions/party-name",
  "type": "string"
}
```
- <a id='catalog-party_reference'>**Party Reference**</a>: References a party defined in metadata.
```json
{
  "title": "Party Reference",
  "description": "References a party defined in metadata.",
  "$id": "#/definitions/party-uuid",
  "type": "string",
  "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
}
```
- <a id='catalog-telephone'>**Telephone**</a>: Contact number by telephone
```json
{
  "title": "Telephone",
  "description": "Contact number by telephone",
  "$id": "#/definitions/phone",
  "type": "object",
  "properties": {
    "type": {
      "description": "Indicates the type of phone number.",
      "type": "string"
    },
    "number": {
      "type": "string"
    }
  },
  "required": [
    "number"
  ],
  "additionalProperties": false
}
```
- <a id='catalog-postal_code'>**Postal Code**</a>: Postal or ZIP code for mailing address
```json
{
  "title": "Postal Code",
  "description": "Postal or ZIP code for mailing address",
  "$id": "#/definitions/postal-code",
  "type": "string"
}
```
- <a id='catalog-property'>**Property**</a>: A value with a name, attributed to the containing control, part, or group.
```json
{
  "title": "Property",
  "description": "A value with a name, attributed to the containing control, part, or group.",
  "$id": "#/definitions/prop",
  "type": "object",
  "properties": {
    "name": {
      "title": "Name",
      "description": "Identifying the purpose and intended use of the property, part or other object.",
      "type": "string"
    },
    "id": {
      "title": "Identifier",
      "description": "Unique identifier of the containing object",
      "type": "string"
    },
    "ns": {
      "title": "Namespace",
      "description": "A namespace qualifying the name.",
      "type": "string"
    },
    "class": {
      "title": "Class",
      "description": "Indicating the type or classification of the containing object",
      "type": "string"
    },
    "value": {
      "type": "string"
    }
  },
  "required": [
    "value",
    "name"
  ],
  "additionalProperties": false
}
```
- <a id='catalog-prose'>**Prose**</a>: Prose permits multiple paragraphs, lists, tables etc.
```json
{
  "title": "Prose",
  "description": "Prose permits multiple paragraphs, lists, tables etc.",
  "$id": "#/definitions/prose",
  "type": "string"
}
```
- <a id='catalog-publication_timestamp'>**Publication Timestamp**</a>: The date and time this document was published.
```json
{
  "title": "Publication Timestamp",
  "description": "The date and time this document was published.",
  "$id": "#/definitions/published",
  "type": "string",
  "format": "date-time",
  "pattern": "^((2000|2400|2800|(19|2[0-9](0[48]|[2468][048]|[13579][26])))-02-29)|(((19|2[0-9])[0-9]{2})-02-(0[1-9]|1[0-9]|2[0-8]))|(((19|2[0-9])[0-9]{2})-(0[13578]|10|12)-(0[1-9]|[12][0-9]|3[01]))|(((19|2[0-9])[0-9]{2})-(0[469]|11)-(0[1-9]|[12][0-9]|30))T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\\.[0-9]+)?(Z|[+-][0-9]{2}:[0-9]{2})$"
}
```
- <a id='catalog-remarks'>**Remarks**</a>: Additional commentary on the parent item.
```json
{
  "title": "Remarks",
  "description": "Additional commentary on the parent item.",
  "$id": "#/definitions/remarks",
  "type": "string"
}
```
- <a id='catalog-resource'>**Resource**</a>: A resource associated with the present document, which may be a pointer to other data or a citation.
```json
{
  "title": "Resource",
  "description": "A resource associated with the present document, which may be a pointer to other data or a citation.",
  "$id": "#/definitions/resource",
  "type": "object",
  "properties": {
    "uuid": {
      "title": "Universally Unique Identifier",
      "description": "A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "title": {
      "$ref": "#/definitions/title"
    },
    "desc": {
      "$ref": "#/definitions/desc"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "document-ids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/doc-id"
      }
    },
    "citation": {
      "$ref": "#/definitions/citation"
    },
    "rlinks": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/rlink"
      }
    },
    "attachments": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/base64"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "uuid"
  ],
  "additionalProperties": false
}
```
- <a id='catalog-responsible_party'>**Responsible Party**</a>: A reference to a set of organizations or persons that have responsibility for performing a referenced role relative to the parent context.
```json
{
  "title": "Responsible Party",
  "description": "A reference to a set of organizations or persons that have responsibility for performing a referenced role relative to the parent context.",
  "$id": "#/definitions/responsible-party",
  "type": "object",
  "properties": {
    "party-uuids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/party-uuid"
      }
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "party-uuids"
  ],
  "additionalProperties": false
}
```
- <a id='catalog-revision_history_entry'>**Revision History Entry**</a>: An entry in a sequential list of revisions to the containing document in reverse chronological order (i.e., most recent previous revision first).
```json
{
  "title": "Revision History Entry",
  "description": "An entry in a sequential list of revisions to the containing document in reverse chronological order (i.e., most recent previous revision first).",
  "$id": "#/definitions/revision",
  "type": "object",
  "properties": {
    "title": {
      "$ref": "#/definitions/title"
    },
    "published": {
      "$ref": "#/definitions/published"
    },
    "last-modified": {
      "$ref": "#/definitions/last-modified"
    },
    "version": {
      "$ref": "#/definitions/version"
    },
    "oscal-version": {
      "$ref": "#/definitions/oscal-version"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "additionalProperties": false
}
```
- <a id='catalog-resource_link'>**Resource link**</a>: A pointer to an external copy of a document with optional hash for verification
```json
{
  "title": "Resource link",
  "description": "A pointer to an external copy of a document with optional hash for verification",
  "$id": "#/definitions/rlink",
  "type": "object",
  "properties": {
    "href": {
      "title": "hypertext reference",
      "description": "A link to a document or document fragment (actual, nominal or projected)",
      "type": "string",
      "format": "uri-reference"
    },
    "media-type": {
      "title": "Media type",
      "description": "Describes the media type of the linked resource",
      "type": "string"
    },
    "hashes": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/hash"
      }
    }
  },
  "required": [
    "href"
  ],
  "additionalProperties": false
}
```
- <a id='catalog-role'>**Role**</a>: Defining a role to be assigned to a party
```json
{
  "title": "Role",
  "description": "Defining a role to be assigned to a party",
  "$id": "#/definitions/role",
  "type": "object",
  "properties": {
    "id": {
      "title": "Identifier",
      "description": "Unique identifier of the containing object",
      "type": "string"
    },
    "title": {
      "$ref": "#/definitions/title"
    },
    "short-name": {
      "$ref": "#/definitions/short-name"
    },
    "desc": {
      "$ref": "#/definitions/desc"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "id",
    "title"
  ],
  "additionalProperties": false
}
```
- <a id='catalog-selection'>**Selection**</a>: Presenting a choice among alternatives
```json
{
  "title": "Selection",
  "description": "Presenting a choice among alternatives",
  "$id": "#/definitions/select",
  "type": "object",
  "properties": {
    "how-many": {
      "title": "Cardinality",
      "description": "When selecting, a requirement such as one or more",
      "type": "string"
    },
    "alternatives": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/choice"
      }
    }
  },
  "additionalProperties": false
}
```
- <a id='catalog-short-name'>**short-name**</a>: A common name, short name or acronym
```json
{
  "title": "short-name",
  "description": "A common name, short name or acronym",
  "$id": "#/definitions/short-name",
  "type": "string"
}
```
- <a id='catalog-state'>**State**</a>: State, province or analogous geographical region for mailing address
```json
{
  "title": "State",
  "description": "State, province or analogous geographical region for mailing address",
  "$id": "#/definitions/state",
  "type": "string"
}
```
- <a id='catalog-text'>**Text**</a>: A line of textual content whose semantic is determined by the context of use.
```json
{
  "title": "Text",
  "description": "A line of textual content whose semantic is determined by the context of use.",
  "$id": "#/definitions/text",
  "type": "string"
}
```
- <a id='catalog-title'>**Title**</a>: A title for display and navigation
```json
{
  "title": "Title",
  "description": "A title for display and navigation",
  "$id": "#/definitions/title",
  "type": "string"
}
```
- <a id='catalog-url'>**URL**</a>: URL for web site or Internet presence
```json
{
  "title": "URL",
  "description": "URL for web site or Internet presence",
  "$id": "#/definitions/url",
  "type": "string",
  "format": "uri"
}
```
- <a id='catalog-parameter_description'>**Parameter description**</a>: Indicates and explains the purpose and use of a parameter
```json
{
  "title": "Parameter description",
  "description": "Indicates and explains the purpose and use of a parameter",
  "$id": "#/definitions/usage",
  "type": "object",
  "properties": {
    "id": {
      "title": "Identifier",
      "description": "Unique identifier of the containing object",
      "type": "string"
    },
    "summary": {
      "type": "string"
    }
  },
  "required": [
    "summary"
  ],
  "additionalProperties": false
}
```
- <a id='catalog-value_constraint'>**Value constraint**</a>: Indicates a permissible value for a parameter or property
```json
{
  "title": "Value constraint",
  "description": "Indicates a permissible value for a parameter or property",
  "$id": "#/definitions/value",
  "type": "string"
}
```
- <a id='catalog-document_version'>**Document version**</a>: The version of the document content.
```json
{
  "title": "Document version",
  "description": "The version of the document content.",
  "$id": "#/definitions/version",
  "type": "string"
}
```

## component

> OSCAL Implementation Component Format

- <a id='component-address_line'>**Address line**</a>: A single line of an address.
```json
{
  "title": "Address line",
  "description": "A single line of an address.",
  "$id": "#/definitions/addr-line",
  "type": "string"
}
```
- <a id='component-address'>**Address**</a>: A postal address.
```json
{
  "title": "Address",
  "description": "A postal address.",
  "$id": "#/definitions/address",
  "type": "object",
  "properties": {
    "type": {
      "description": "Indicates the type of address.",
      "type": "string"
    },
    "postal-address": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/addr-line"
      }
    },
    "city": {
      "$ref": "#/definitions/city"
    },
    "state": {
      "$ref": "#/definitions/state"
    },
    "postal-code": {
      "$ref": "#/definitions/postal-code"
    },
    "country": {
      "$ref": "#/definitions/country"
    }
  },
  "additionalProperties": false
}
```
- <a id='component-annotation'>**Annotation**</a>: A name/value pair with optional explanatory remarks.
```json
{
  "title": "Annotation",
  "description": "A name/value pair with optional explanatory remarks.",
  "$id": "#/definitions/annotation",
  "type": "object",
  "properties": {
    "name": {
      "title": "Name",
      "description": "Identifying the purpose and intended use of the property, part or other object.",
      "type": "string"
    },
    "id": {
      "title": "Identifier",
      "description": "Unique identifier of the containing object",
      "type": "string"
    },
    "ns": {
      "title": "Namespace",
      "description": "A namespace qualifying the name.",
      "type": "string"
    },
    "value": {
      "title": "Value",
      "description": "Indicates the value of the characteristic.",
      "type": "string"
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "name"
  ],
  "additionalProperties": false
}
```
- <a id='component-back_matter'>**Back matter**</a>: A collection of citations and resource references.
```json
{
  "title": "Back matter",
  "description": "A collection of citations and resource references.",
  "$id": "#/definitions/back-matter",
  "type": "object",
  "properties": {
    "resources": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/resource"
      }
    }
  },
  "additionalProperties": false
}
```
- <a id='component-base64'>**Base64**</a>: 
```json
{
  "title": "Base64",
  "description": "",
  "$id": "#/definitions/base64",
  "type": "object",
  "properties": {
    "filename": {
      "title": "File Name",
      "description": "Name of the file before it was encoded as Base64 to be embedded in a resource. This is the name that will be assigned to the file when the file is decoded.",
      "type": "string",
      "format": "uri-reference"
    },
    "media-type": {
      "title": "Media type",
      "description": "Describes the media type of the linked resource",
      "type": "string"
    },
    "value": {
      "type": "string"
    }
  },
  "required": [
    "value"
  ],
  "additionalProperties": false
}
```
- <a id='component-bibliographic_definition'>**Bibliographic Definition**</a>: A container in which a set of bibliographic information can included. The model of this information is undefined by OSCAL.
```json
{
  "title": "Bibliographic Definition",
  "description": "A container in which a set of bibliographic information can included. The model of this information is undefined by OSCAL.",
  "$id": "#/definitions/biblio",
  "type": "object",
  "additionalProperties": false
}
```
- <a id='component-capability'>**Capability**</a>: A grouping of other components and/or capabilities.
```json
{
  "title": "Capability",
  "description": "A grouping of other components and/or capabilities.",
  "$id": "#/definitions/capability",
  "type": "object",
  "properties": {
    "name": {
      "title": "Capability Name",
      "description": "The capability's human-readable name.",
      "type": "string"
    },
    "description": {
      "$ref": "#/definitions/description"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "incorporates-components": {
      "type": "object",
      "minProperties": 1,
      "additionalProperties": {
        "allOf": [
          {
            "type": "object",
            "$ref": "#/definitions/incorporates-component"
          },
          {
            "not": {
              "type": "string"
            }
          }
        ]
      }
    },
    "control-implementations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/control-implementation"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "name",
    "description"
  ],
  "additionalProperties": false
}
```
- <a id='component-citation'>**Citation**</a>: A citation consisting of end note text and optional structured bibliographic data.
```json
{
  "title": "Citation",
  "description": "A citation consisting of end note text and optional structured bibliographic data.",
  "$id": "#/definitions/citation",
  "type": "object",
  "properties": {
    "text": {
      "$ref": "#/definitions/text"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "biblio": {
      "$ref": "#/definitions/biblio"
    }
  },
  "required": [
    "text"
  ],
  "additionalProperties": false
}
```
- <a id='component-city'>**City**</a>: City, town or geographical region for mailing address
```json
{
  "title": "City",
  "description": "City, town or geographical region for mailing address",
  "$id": "#/definitions/city",
  "type": "string"
}
```
- <a id='component-component'>**Component**</a>: A defined component that can be part of an implemented system.
```json
{
  "title": "Component",
  "description": "A defined component that can be part of an implemented system.",
  "$id": "#/definitions/component",
  "type": "object",
  "properties": {
    "name": {
      "title": "Component Name",
      "description": "The component's short, human-readable name.",
      "type": "string"
    },
    "component-type": {
      "title": "Component Type",
      "description": "A category describing the purpose of the component.",
      "type": "string"
    },
    "title": {
      "$ref": "#/definitions/title"
    },
    "description": {
      "$ref": "#/definitions/description"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "responsible-parties": {
      "type": "object",
      "minProperties": 1,
      "additionalProperties": {
        "allOf": [
          {
            "type": "object",
            "$ref": "#/definitions/responsible-party"
          },
          {
            "not": {
              "type": "string"
            }
          }
        ]
      }
    },
    "control-implementations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/control-implementation"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "name",
    "component-type",
    "title",
    "description"
  ],
  "additionalProperties": false
}
```
- <a id='component-component_definition'>**Component Definition**</a>: A collection of component descriptions, which may optionally be grouped by capability.
```json
{
  "title": "Component Definition",
  "description": "A collection of component descriptions, which may optionally be grouped by capability.",
  "$id": "#/definitions/component-definition",
  "type": "object",
  "properties": {
    "metadata": {
      "$ref": "#/definitions/metadata"
    },
    "import-component-definitions": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/import-component-definition"
      }
    },
    "components": {
      "type": "object",
      "minProperties": 1,
      "additionalProperties": {
        "allOf": [
          {
            "type": "object",
            "$ref": "#/definitions/component"
          },
          {
            "not": {
              "type": "string"
            }
          }
        ]
      }
    },
    "capabilities": {
      "type": "object",
      "minProperties": 1,
      "additionalProperties": {
        "allOf": [
          {
            "type": "object",
            "$ref": "#/definitions/capability"
          },
          {
            "not": {
              "type": "string"
            }
          }
        ]
      }
    },
    "back-matter": {
      "$ref": "#/definitions/back-matter"
    }
  },
  "required": [
    "metadata"
  ],
  "additionalProperties": false
}
```
- <a id='component-control_implementation'>**Control Implementation**</a>: Defines how the component or capability supports a set of controls.
```json
{
  "title": "Control Implementation",
  "description": "Defines how the component or capability supports a set of controls.",
  "$id": "#/definitions/control-implementation",
  "type": "object",
  "properties": {
    "uuid": {
      "title": "Control Implementation Set Identifier",
      "description": "A unique identifier for the set of implemented controls.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "source": {
      "description": "A URL reference to the source catalog or profile for which this component is implementing controls for.",
      "type": "string",
      "format": "uri-reference"
    },
    "description": {
      "$ref": "#/definitions/description"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "implemented-requirements": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/implemented-requirement"
      }
    }
  },
  "required": [
    "uuid",
    "source",
    "description",
    "implemented-requirements"
  ],
  "additionalProperties": false
}
```
- <a id='component-country'>**Country**</a>: Country for mailing address
```json
{
  "title": "Country",
  "description": "Country for mailing address",
  "$id": "#/definitions/country",
  "type": "string"
}
```
- <a id='component-description'>**Description**</a>: A short textual description
```json
{
  "title": "Description",
  "description": "A short textual description",
  "$id": "#/definitions/desc",
  "type": "string"
}
```
- <a id='component-description'>**Description**</a>: A description supporting the parent item.
```json
{
  "title": "Description",
  "description": "A description supporting the parent item.",
  "$id": "#/definitions/description",
  "type": "string"
}
```
- <a id='component-document_identifier'>**Document Identifier**</a>: A document identifier qualified by an identifier type.
```json
{
  "title": "Document Identifier",
  "description": "A document identifier qualified by an identifier type.",
  "$id": "#/definitions/doc-id",
  "type": "object",
  "properties": {
    "type": {
      "description": "Qualifies the kind of document identifier.",
      "type": "string"
    },
    "identifier": {
      "type": "string"
    }
  },
  "required": [
    "identifier",
    "type"
  ],
  "additionalProperties": false
}
```
- <a id='component-email'>**Email**</a>: Email address
```json
{
  "title": "Email",
  "description": "Email address",
  "$id": "#/definitions/email",
  "type": "string",
  "format": "email",
  "pattern": "^.+@.+"
}
```
- <a id='component-personal_identifier'>**Personal Identifier**</a>: An identifier for a person (such as an ORCID) using a designated scheme.
```json
{
  "title": "Personal Identifier",
  "description": "An identifier for a person (such as an ORCID) using a designated scheme.",
  "$id": "#/definitions/external-id",
  "type": "object",
  "properties": {
    "type": {
      "title": "Type",
      "description": "Indicating the type of identifier, address, email or other data item.",
      "type": "string"
    },
    "id": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "type"
  ],
  "additionalProperties": false
}
```
- <a id='component-hash'>**Hash**</a>: A representation of a cryptographic digest generated over a resource using a hash algorithm.
```json
{
  "title": "Hash",
  "description": "A representation of a cryptographic digest generated over a resource using a hash algorithm.",
  "$id": "#/definitions/hash",
  "type": "object",
  "properties": {
    "algorithm": {
      "title": "Hash algorithm",
      "description": "Method by which a hash is derived",
      "type": "string"
    },
    "value": {
      "type": "string"
    }
  },
  "required": [
    "value",
    "algorithm"
  ],
  "additionalProperties": false
}
```
- <a id='component-control-based_requirement'>**Control-based Requirement**</a>: Describes how the component implements an individual control.
```json
{
  "title": "Control-based Requirement",
  "description": "Describes how the component implements an individual control.",
  "$id": "#/definitions/implemented-requirement",
  "type": "object",
  "properties": {
    "uuid": {
      "title": "Universally Unique Identifier",
      "description": "A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "control-id": {
      "title": "Control Identifier Reference",
      "description": "A reference to a control identifier.",
      "type": "string"
    },
    "description": {
      "$ref": "#/definitions/description"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "responsible-roles": {
      "type": "object",
      "minProperties": 1,
      "additionalProperties": {
        "allOf": [
          {
            "type": "object",
            "$ref": "#/definitions/responsible-role"
          },
          {
            "not": {
              "type": "string"
            }
          }
        ]
      }
    },
    "set-parameters": {
      "type": "object",
      "minProperties": 1,
      "additionalProperties": {
        "allOf": [
          {
            "type": "object",
            "$ref": "#/definitions/set-parameter"
          },
          {
            "not": {
              "type": "string"
            }
          }
        ]
      }
    },
    "statements": {
      "type": "object",
      "minProperties": 1,
      "additionalProperties": {
        "allOf": [
          {
            "type": "object",
            "$ref": "#/definitions/statement"
          },
          {
            "not": {
              "type": "string"
            }
          }
        ]
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "uuid"
  ],
  "additionalProperties": false
}
```
- <a id='component-import_component_definition'>**Import Component Definition**</a>: Loads a component definition from another resource.
```json
{
  "title": "Import Component Definition",
  "description": "Loads a component definition from another resource.",
  "$id": "#/definitions/import-component-definition",
  "type": "object",
  "properties": {
    "href": {
      "title": "Hyperlink Reference",
      "description": "A link to a resource that defines a set of components and/or capabilities to import into this collection.",
      "type": "string",
      "format": "uri-reference"
    }
  },
  "required": [
    "href"
  ],
  "additionalProperties": false
}
```
- <a id='component-incorporates_component'>**Incorporates Component**</a>: TBD
```json
{
  "title": "Incorporates Component",
  "description": "TBD",
  "$id": "#/definitions/incorporates-component",
  "type": "object",
  "properties": {
    "description": {
      "$ref": "#/definitions/description"
    }
  },
  "required": [
    "description"
  ],
  "additionalProperties": false
}
```
- <a id='component-last_modified_timestamp'>**Last modified timestamp**</a>: Date and time of last modification.
```json
{
  "title": "Last modified timestamp",
  "description": "Date and time of last modification.",
  "$id": "#/definitions/last-modified",
  "type": "string",
  "format": "date-time",
  "pattern": "^((2000|2400|2800|(19|2[0-9](0[48]|[2468][048]|[13579][26])))-02-29)|(((19|2[0-9])[0-9]{2})-02-(0[1-9]|1[0-9]|2[0-8]))|(((19|2[0-9])[0-9]{2})-(0[13578]|10|12)-(0[1-9]|[12][0-9]|3[01]))|(((19|2[0-9])[0-9]{2})-(0[469]|11)-(0[1-9]|[12][0-9]|30))T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\\.[0-9]+)?(Z|[+-][0-9]{2}:[0-9]{2})$"
}
```
- <a id='component-link'>**Link**</a>: A reference to a local or remote resource
```json
{
  "title": "Link",
  "description": "A reference to a local or remote resource",
  "$id": "#/definitions/link",
  "type": "object",
  "properties": {
    "href": {
      "title": "hypertext reference",
      "description": "A link to a document or document fragment (actual, nominal or projected)",
      "type": "string",
      "format": "uri-reference"
    },
    "rel": {
      "title": "Relation",
      "description": "Describes the type of relationship provided by the link. This can be an indicator of the link's purpose.",
      "type": "string"
    },
    "media-type": {
      "title": "Media type",
      "description": "Describes the media type of the linked resource",
      "type": "string"
    },
    "text": {
      "type": "string"
    }
  },
  "required": [
    "text",
    "href"
  ],
  "additionalProperties": false
}
```
- <a id='component-location'>**Location**</a>: A location, with associated metadata that can be referenced.
```json
{
  "title": "Location",
  "description": "A location, with associated metadata that can be referenced.",
  "$id": "#/definitions/location",
  "type": "object",
  "properties": {
    "uuid": {
      "title": "Universally Unique Identifier",
      "description": "A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "title": {
      "$ref": "#/definitions/title"
    },
    "address": {
      "$ref": "#/definitions/address"
    },
    "email-addresses": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/email"
      }
    },
    "telephone-numbers": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/phone"
      }
    },
    "URLs": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/url"
      }
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "uuid",
    "address"
  ],
  "additionalProperties": false
}
```
- <a id='component-location_reference'>**Location Reference**</a>: References a location defined in metadata.
```json
{
  "title": "Location Reference",
  "description": "References a location defined in metadata.",
  "$id": "#/definitions/location-uuid",
  "type": "string",
  "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
}
```
- <a id='component-organizational_affiliation'>**Organizational Affiliation**</a>: Identifies that the containing object is a member of the organization associated with the provided UUID.
```json
{
  "title": "Organizational Affiliation",
  "description": "Identifies that the containing object is a member of the organization associated with the provided UUID.",
  "$id": "#/definitions/member-of-organization",
  "type": "string",
  "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
}
```
- <a id='component-publication_metadata'>**Publication metadata**</a>: Provides information about the publication and availability of the containing document.
```json
{
  "title": "Publication metadata",
  "description": "Provides information about the publication and availability of the containing document.",
  "$id": "#/definitions/metadata",
  "type": "object",
  "properties": {
    "title": {
      "$ref": "#/definitions/title"
    },
    "published": {
      "$ref": "#/definitions/published"
    },
    "last-modified": {
      "$ref": "#/definitions/last-modified"
    },
    "version": {
      "$ref": "#/definitions/version"
    },
    "oscal-version": {
      "$ref": "#/definitions/oscal-version"
    },
    "revision-history": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/revision"
      }
    },
    "document-ids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/doc-id"
      }
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "roles": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/role"
      }
    },
    "locations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/location"
      }
    },
    "parties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/party"
      }
    },
    "responsible-parties": {
      "type": "object",
      "minProperties": 1,
      "additionalProperties": {
        "allOf": [
          {
            "type": "object",
            "$ref": "#/definitions/responsible-party"
          },
          {
            "not": {
              "type": "string"
            }
          }
        ]
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "title",
    "last-modified",
    "version",
    "oscal-version"
  ],
  "additionalProperties": false
}
```
- <a id='component-oscal_version'>**OSCAL version**</a>: OSCAL model version.
```json
{
  "title": "OSCAL version",
  "description": "OSCAL model version.",
  "$id": "#/definitions/oscal-version",
  "type": "string"
}
```
- <a id='component-party_(organization_or_person)'>**Party (organization or person)**</a>: A responsible entity, either singular (an organization or person) or collective (multiple persons)
```json
{
  "title": "Party (organization or person)",
  "description": "A responsible entity, either singular (an organization or person) or collective (multiple persons)",
  "$id": "#/definitions/party",
  "type": "object",
  "properties": {
    "uuid": {
      "title": "Universally Unique Identifier",
      "description": "A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "type": {
      "title": "Party Type",
      "description": "A category describing the kind of party the object describes.",
      "type": "string",
      "enum": [
        "person",
        "organization"
      ]
    },
    "party-name": {
      "$ref": "#/definitions/party-name"
    },
    "short-name": {
      "$ref": "#/definitions/short-name"
    },
    "external-ids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/external-id"
      }
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "addresses": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/address"
      }
    },
    "email-addresses": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/email"
      }
    },
    "telephone-numbers": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/phone"
      }
    },
    "member-of-organizations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/member-of-organization"
      }
    },
    "location-uuids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/location-uuid"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "uuid",
    "type",
    "party-name"
  ],
  "additionalProperties": false
}
```
- <a id='component-party_name'>**Party Name**</a>: The full (legal) name of the party.
```json
{
  "title": "Party Name",
  "description": "The full (legal) name of the party.",
  "$id": "#/definitions/party-name",
  "type": "string"
}
```
- <a id='component-party_reference'>**Party Reference**</a>: References a party defined in metadata.
```json
{
  "title": "Party Reference",
  "description": "References a party defined in metadata.",
  "$id": "#/definitions/party-uuid",
  "type": "string",
  "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
}
```
- <a id='component-telephone'>**Telephone**</a>: Contact number by telephone
```json
{
  "title": "Telephone",
  "description": "Contact number by telephone",
  "$id": "#/definitions/phone",
  "type": "object",
  "properties": {
    "type": {
      "description": "Indicates the type of phone number.",
      "type": "string"
    },
    "number": {
      "type": "string"
    }
  },
  "required": [
    "number"
  ],
  "additionalProperties": false
}
```
- <a id='component-postal_code'>**Postal Code**</a>: Postal or ZIP code for mailing address
```json
{
  "title": "Postal Code",
  "description": "Postal or ZIP code for mailing address",
  "$id": "#/definitions/postal-code",
  "type": "string"
}
```
- <a id='component-property'>**Property**</a>: A value with a name, attributed to the containing control, part, or group.
```json
{
  "title": "Property",
  "description": "A value with a name, attributed to the containing control, part, or group.",
  "$id": "#/definitions/prop",
  "type": "object",
  "properties": {
    "name": {
      "title": "Name",
      "description": "Identifying the purpose and intended use of the property, part or other object.",
      "type": "string"
    },
    "id": {
      "title": "Identifier",
      "description": "Unique identifier of the containing object",
      "type": "string"
    },
    "ns": {
      "title": "Namespace",
      "description": "A namespace qualifying the name.",
      "type": "string"
    },
    "class": {
      "title": "Class",
      "description": "Indicating the type or classification of the containing object",
      "type": "string"
    },
    "value": {
      "type": "string"
    }
  },
  "required": [
    "value",
    "name"
  ],
  "additionalProperties": false
}
```
- <a id='component-publication_timestamp'>**Publication Timestamp**</a>: The date and time this document was published.
```json
{
  "title": "Publication Timestamp",
  "description": "The date and time this document was published.",
  "$id": "#/definitions/published",
  "type": "string",
  "format": "date-time",
  "pattern": "^((2000|2400|2800|(19|2[0-9](0[48]|[2468][048]|[13579][26])))-02-29)|(((19|2[0-9])[0-9]{2})-02-(0[1-9]|1[0-9]|2[0-8]))|(((19|2[0-9])[0-9]{2})-(0[13578]|10|12)-(0[1-9]|[12][0-9]|3[01]))|(((19|2[0-9])[0-9]{2})-(0[469]|11)-(0[1-9]|[12][0-9]|30))T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\\.[0-9]+)?(Z|[+-][0-9]{2}:[0-9]{2})$"
}
```
- <a id='component-remarks'>**Remarks**</a>: Additional commentary on the parent item.
```json
{
  "title": "Remarks",
  "description": "Additional commentary on the parent item.",
  "$id": "#/definitions/remarks",
  "type": "string"
}
```
- <a id='component-resource'>**Resource**</a>: A resource associated with the present document, which may be a pointer to other data or a citation.
```json
{
  "title": "Resource",
  "description": "A resource associated with the present document, which may be a pointer to other data or a citation.",
  "$id": "#/definitions/resource",
  "type": "object",
  "properties": {
    "uuid": {
      "title": "Universally Unique Identifier",
      "description": "A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "title": {
      "$ref": "#/definitions/title"
    },
    "desc": {
      "$ref": "#/definitions/desc"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "document-ids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/doc-id"
      }
    },
    "citation": {
      "$ref": "#/definitions/citation"
    },
    "rlinks": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/rlink"
      }
    },
    "attachments": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/base64"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "uuid"
  ],
  "additionalProperties": false
}
```
- <a id='component-responsible_party'>**Responsible Party**</a>: A reference to a set of organizations or persons that have responsibility for performing a referenced role relative to the parent context.
```json
{
  "title": "Responsible Party",
  "description": "A reference to a set of organizations or persons that have responsibility for performing a referenced role relative to the parent context.",
  "$id": "#/definitions/responsible-party",
  "type": "object",
  "properties": {
    "party-uuids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/party-uuid"
      }
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "party-uuids"
  ],
  "additionalProperties": false
}
```
- <a id='component-responsible_role'>**Responsible Role**</a>: A reference to one or more roles with responsibility for performing a function relative to the control.
```json
{
  "title": "Responsible Role",
  "description": "A reference to one or more roles with responsibility for performing a function relative to the control.",
  "$id": "#/definitions/responsible-role",
  "type": "object",
  "properties": {
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "party-ids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/party-uuid"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "additionalProperties": false
}
```
- <a id='component-revision_history_entry'>**Revision History Entry**</a>: An entry in a sequential list of revisions to the containing document in reverse chronological order (i.e., most recent previous revision first).
```json
{
  "title": "Revision History Entry",
  "description": "An entry in a sequential list of revisions to the containing document in reverse chronological order (i.e., most recent previous revision first).",
  "$id": "#/definitions/revision",
  "type": "object",
  "properties": {
    "title": {
      "$ref": "#/definitions/title"
    },
    "published": {
      "$ref": "#/definitions/published"
    },
    "last-modified": {
      "$ref": "#/definitions/last-modified"
    },
    "version": {
      "$ref": "#/definitions/version"
    },
    "oscal-version": {
      "$ref": "#/definitions/oscal-version"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "additionalProperties": false
}
```
- <a id='component-resource_link'>**Resource link**</a>: A pointer to an external copy of a document with optional hash for verification
```json
{
  "title": "Resource link",
  "description": "A pointer to an external copy of a document with optional hash for verification",
  "$id": "#/definitions/rlink",
  "type": "object",
  "properties": {
    "href": {
      "title": "hypertext reference",
      "description": "A link to a document or document fragment (actual, nominal or projected)",
      "type": "string",
      "format": "uri-reference"
    },
    "media-type": {
      "title": "Media type",
      "description": "Describes the media type of the linked resource",
      "type": "string"
    },
    "hashes": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/hash"
      }
    }
  },
  "required": [
    "href"
  ],
  "additionalProperties": false
}
```
- <a id='component-role'>**Role**</a>: Defining a role to be assigned to a party
```json
{
  "title": "Role",
  "description": "Defining a role to be assigned to a party",
  "$id": "#/definitions/role",
  "type": "object",
  "properties": {
    "id": {
      "title": "Identifier",
      "description": "Unique identifier of the containing object",
      "type": "string"
    },
    "title": {
      "$ref": "#/definitions/title"
    },
    "short-name": {
      "$ref": "#/definitions/short-name"
    },
    "desc": {
      "$ref": "#/definitions/desc"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "id",
    "title"
  ],
  "additionalProperties": false
}
```
- <a id='component-set_parameter_value'>**Set Parameter Value**</a>: Identifies the parameter that will be filled in by the enclosed value element.
```json
{
  "title": "Set Parameter Value",
  "description": "Identifies the parameter that will be filled in by the enclosed value element.",
  "$id": "#/definitions/set-parameter",
  "type": "object",
  "properties": {
    "value": {
      "$ref": "#/definitions/value"
    }
  },
  "required": [
    "value"
  ],
  "additionalProperties": false
}
```
- <a id='component-short-name'>**short-name**</a>: A common name, short name or acronym
```json
{
  "title": "short-name",
  "description": "A common name, short name or acronym",
  "$id": "#/definitions/short-name",
  "type": "string"
}
```
- <a id='component-state'>**State**</a>: State, province or analogous geographical region for mailing address
```json
{
  "title": "State",
  "description": "State, province or analogous geographical region for mailing address",
  "$id": "#/definitions/state",
  "type": "string"
}
```
- <a id='component-specific_statement'>**Specific Statement**</a>: Identifies which statements within a control are addressed.
```json
{
  "title": "Specific Statement",
  "description": "Identifies which statements within a control are addressed.",
  "$id": "#/definitions/statement",
  "type": "object",
  "properties": {
    "uuid": {
      "title": "Universally Unique Identifier",
      "description": "A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "description": {
      "$ref": "#/definitions/description"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "anyOf": [
        {
          "$ref": "#/definitions/annotation"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/annotation"
          },
          "minItems": 2
        }
      ]
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "responsible-roles": {
      "type": "object",
      "minProperties": 1,
      "additionalProperties": {
        "allOf": [
          {
            "type": "object",
            "$ref": "#/definitions/responsible-role"
          },
          {
            "not": {
              "type": "string"
            }
          }
        ]
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "uuid"
  ],
  "additionalProperties": false
}
```
- <a id='component-text'>**Text**</a>: A line of textual content whose semantic is determined by the context of use.
```json
{
  "title": "Text",
  "description": "A line of textual content whose semantic is determined by the context of use.",
  "$id": "#/definitions/text",
  "type": "string"
}
```
- <a id='component-title'>**Title**</a>: A title for display and navigation
```json
{
  "title": "Title",
  "description": "A title for display and navigation",
  "$id": "#/definitions/title",
  "type": "string"
}
```
- <a id='component-url'>**URL**</a>: URL for web site or Internet presence
```json
{
  "title": "URL",
  "description": "URL for web site or Internet presence",
  "$id": "#/definitions/url",
  "type": "string",
  "format": "uri"
}
```
- <a id='component-value'>**Value**</a>: The phrase or string that fills-in the parameter and completes the requirement statement.
```json
{
  "title": "Value",
  "description": "The phrase or string that fills-in the parameter and completes the requirement statement.",
  "$id": "#/definitions/value",
  "type": "string"
}
```
- <a id='component-document_version'>**Document version**</a>: The version of the document content.
```json
{
  "title": "Document version",
  "description": "The version of the document content.",
  "$id": "#/definitions/version",
  "type": "string"
}
```

## poam

> OSCAL Plan of Action and Milestones (POA&M) Format

- <a id='poam-activity_id'>**Activity ID**</a>: Links the task to a defined activity.
```json
{
  "title": "Activity ID",
  "description": "Links the task to a defined activity.",
  "$id": "#/definitions/activity-uuid",
  "type": "string",
  "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
}
```
- <a id='poam-address_line'>**Address line**</a>: A single line of an address.
```json
{
  "title": "Address line",
  "description": "A single line of an address.",
  "$id": "#/definitions/addr-line",
  "type": "string"
}
```
- <a id='poam-address'>**Address**</a>: A postal address.
```json
{
  "title": "Address",
  "description": "A postal address.",
  "$id": "#/definitions/address",
  "type": "object",
  "properties": {
    "type": {
      "description": "Indicates the type of address.",
      "type": "string"
    },
    "postal-address": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/addr-line"
      }
    },
    "city": {
      "$ref": "#/definitions/city"
    },
    "state": {
      "$ref": "#/definitions/state"
    },
    "postal-code": {
      "$ref": "#/definitions/postal-code"
    },
    "country": {
      "$ref": "#/definitions/country"
    }
  },
  "additionalProperties": false
}
```
- <a id='poam-annotation'>**Annotation**</a>: A name/value pair with optional explanatory remarks.
```json
{
  "title": "Annotation",
  "description": "A name/value pair with optional explanatory remarks.",
  "$id": "#/definitions/annotation",
  "type": "object",
  "properties": {
    "name": {
      "title": "Name",
      "description": "Identifying the purpose and intended use of the property, part or other object.",
      "type": "string"
    },
    "id": {
      "title": "Identifier",
      "description": "Unique identifier of the containing object",
      "type": "string"
    },
    "ns": {
      "title": "Namespace",
      "description": "A namespace qualifying the name.",
      "type": "string"
    },
    "value": {
      "title": "Value",
      "description": "Indicates the value of the characteristic.",
      "type": "string"
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "name"
  ],
  "additionalProperties": false
}
```
- <a id='poam-assessor'>**Assessor**</a>: Identifies an individual who gathered the evidence resulting in the observation or risk identification.
```json
{
  "title": "Assessor",
  "description": "Identifies an individual who gathered the evidence resulting in the observation or risk identification.",
  "$id": "#/definitions/assessor",
  "type": "object",
  "properties": {
    "party-uuid": {
      "title": "Party UUID",
      "description": "The UUID of the assessor who collected the evidence or made the observation.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "STRVALUE": {
      "type": "string"
    }
  },
  "required": [
    "STRVALUE",
    "party-uuid"
  ],
  "additionalProperties": false
}
```
- <a id='poam-back_matter'>**Back matter**</a>: A collection of citations and resource references.
```json
{
  "title": "Back matter",
  "description": "A collection of citations and resource references.",
  "$id": "#/definitions/back-matter",
  "type": "object",
  "properties": {
    "resources": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/resource"
      }
    }
  },
  "additionalProperties": false
}
```
- <a id='poam-base64'>**Base64**</a>: 
```json
{
  "title": "Base64",
  "description": "",
  "$id": "#/definitions/base64",
  "type": "object",
  "properties": {
    "filename": {
      "title": "File Name",
      "description": "Name of the file before it was encoded as Base64 to be embedded in a resource. This is the name that will be assigned to the file when the file is decoded.",
      "type": "string",
      "format": "uri-reference"
    },
    "media-type": {
      "title": "Media type",
      "description": "Describes the media type of the linked resource",
      "type": "string"
    },
    "value": {
      "type": "string"
    }
  },
  "required": [
    "value"
  ],
  "additionalProperties": false
}
```
- <a id='poam-bibliographic_definition'>**Bibliographic Definition**</a>: A container in which a set of bibliographic information can included. The model of this information is undefined by OSCAL.
```json
{
  "title": "Bibliographic Definition",
  "description": "A container in which a set of bibliographic information can included. The model of this information is undefined by OSCAL.",
  "$id": "#/definitions/biblio",
  "type": "object",
  "additionalProperties": false
}
```
- <a id='poam-citation'>**Citation**</a>: A citation consisting of end note text and optional structured bibliographic data.
```json
{
  "title": "Citation",
  "description": "A citation consisting of end note text and optional structured bibliographic data.",
  "$id": "#/definitions/citation",
  "type": "object",
  "properties": {
    "text": {
      "$ref": "#/definitions/text"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "biblio": {
      "$ref": "#/definitions/biblio"
    }
  },
  "required": [
    "text"
  ],
  "additionalProperties": false
}
```
- <a id='poam-city'>**City**</a>: City, town or geographical region for mailing address
```json
{
  "title": "City",
  "description": "City, town or geographical region for mailing address",
  "$id": "#/definitions/city",
  "type": "string"
}
```
- <a id='poam-closer_actions'>**Closer Actions**</a>: Describes the actions taken that resulted in the closure of the identified risk.
```json
{
  "title": "Closer Actions",
  "description": "Describes the actions taken that resulted in the closure of the identified risk.",
  "$id": "#/definitions/closure-actions",
  "type": "string"
}
```
- <a id='poam-compare_to'>**Compare To**</a>: Typically used in when copying content from the assessment plan to the assessment results. The uuid should be changed in the assessment results file, and the compare-to field should be set to the original assessment plan uuid value. This enables the plan and results to be compared later to identify what changed between the two.
```json
{
  "title": "Compare To",
  "description": "Typically used in when copying content from the assessment plan to the assessment results. The uuid should be changed in the assessment results file, and the compare-to field should be set to the original assessment plan uuid value. This enables the plan and results to be compared later to identify what changed between the two.",
  "$id": "#/definitions/compare-to",
  "type": "string"
}
```
- <a id='poam-component'>**Component**</a>: A defined component that can be part of an implemented system.
```json
{
  "title": "Component",
  "description": "A defined component that can be part of an implemented system.",
  "$id": "#/definitions/component",
  "type": "object",
  "properties": {
    "component-type": {
      "title": "Component Type",
      "description": "A category describing the purpose of the component.",
      "type": "string"
    },
    "title": {
      "$ref": "#/definitions/title"
    },
    "description": {
      "$ref": "#/definitions/description"
    },
    "purpose": {
      "$ref": "#/definitions/purpose"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "status": {
      "$ref": "#/definitions/status"
    },
    "responsible-roles": {
      "type": "object",
      "minProperties": 1,
      "additionalProperties": {
        "allOf": [
          {
            "type": "object",
            "$ref": "#/definitions/responsible-role"
          },
          {
            "not": {
              "type": "string"
            }
          }
        ]
      }
    },
    "protocols": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/protocol"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "component-type",
    "title",
    "description",
    "status"
  ],
  "additionalProperties": false
}
```
- <a id='poam-country'>**Country**</a>: Country for mailing address
```json
{
  "title": "Country",
  "description": "Country for mailing address",
  "$id": "#/definitions/country",
  "type": "string"
}
```
- <a id='poam-date/time_stamp'>**Date/Time Stamp**</a>: Date/time stamp identifying when the information was collected.
```json
{
  "title": "Date/Time Stamp",
  "description": "Date/time stamp identifying when the information was collected.",
  "$id": "#/definitions/date-time-stamp",
  "type": "string",
  "format": "date-time",
  "pattern": "^((2000|2400|2800|(19|2[0-9](0[48]|[2468][048]|[13579][26])))-02-29)|(((19|2[0-9])[0-9]{2})-02-(0[1-9]|1[0-9]|2[0-8]))|(((19|2[0-9])[0-9]{2})-(0[13578]|10|12)-(0[1-9]|[12][0-9]|3[01]))|(((19|2[0-9])[0-9]{2})-(0[469]|11)-(0[1-9]|[12][0-9]|30))T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\\.[0-9]+)?(Z|[+-][0-9]{2}:[0-9]{2})$"
}
```
- <a id='poam-description'>**Description**</a>: A short textual description
```json
{
  "title": "Description",
  "description": "A short textual description",
  "$id": "#/definitions/desc",
  "type": "string"
}
```
- <a id='poam-description'>**Description**</a>: A description supporting the parent item.
```json
{
  "title": "Description",
  "description": "A description supporting the parent item.",
  "$id": "#/definitions/description",
  "type": "string"
}
```
- <a id='poam-document_identifier'>**Document Identifier**</a>: A document identifier qualified by an identifier type.
```json
{
  "title": "Document Identifier",
  "description": "A document identifier qualified by an identifier type.",
  "$id": "#/definitions/doc-id",
  "type": "object",
  "properties": {
    "type": {
      "description": "Qualifies the kind of document identifier.",
      "type": "string"
    },
    "identifier": {
      "type": "string"
    }
  },
  "required": [
    "identifier",
    "type"
  ],
  "additionalProperties": false
}
```
- <a id='poam-email'>**Email**</a>: Email address
```json
{
  "title": "Email",
  "description": "Email address",
  "$id": "#/definitions/email",
  "type": "string",
  "format": "email",
  "pattern": "^.+@.+"
}
```
- <a id='poam-end'>**End**</a>: Identifies the end of a task.
```json
{
  "title": "End",
  "description": "Identifies the end of a task.",
  "$id": "#/definitions/end",
  "type": "string",
  "format": "date-time",
  "pattern": "^((2000|2400|2800|(19|2[0-9](0[48]|[2468][048]|[13579][26])))-02-29)|(((19|2[0-9])[0-9]{2})-02-(0[1-9]|1[0-9]|2[0-8]))|(((19|2[0-9])[0-9]{2})-(0[13578]|10|12)-(0[1-9]|[12][0-9]|3[01]))|(((19|2[0-9])[0-9]{2})-(0[469]|11)-(0[1-9]|[12][0-9]|30))T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\\.[0-9]+)?(Z|[+-][0-9]{2}:[0-9]{2})$"
}
```
- <a id='poam-personal_identifier'>**Personal Identifier**</a>: An identifier for a person (such as an ORCID) using a designated scheme.
```json
{
  "title": "Personal Identifier",
  "description": "An identifier for a person (such as an ORCID) using a designated scheme.",
  "$id": "#/definitions/external-id",
  "type": "object",
  "properties": {
    "type": {
      "title": "Type",
      "description": "Indicating the type of identifier, address, email or other data item.",
      "type": "string"
    },
    "id": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "type"
  ],
  "additionalProperties": false
}
```
- <a id='poam-finding'>**Finding**</a>: Describes an individual finding.
```json
{
  "title": "Finding",
  "description": "Describes an individual finding.",
  "$id": "#/definitions/finding",
  "type": "object",
  "properties": {
    "uuid": {
      "title": "Universally Unique Identifier",
      "description": "A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "title": {
      "$ref": "#/definitions/title"
    },
    "description": {
      "$ref": "#/definitions/description"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "date-time-stamp": {
      "$ref": "#/definitions/date-time-stamp"
    },
    "objective-status": {
      "$ref": "#/definitions/objective-status"
    },
    "implementation-statement-uuid": {
      "$ref": "#/definitions/implementation-statement-uuid"
    },
    "observations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/observation"
      }
    },
    "threat-ids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/threat-id"
      }
    },
    "risks": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/risk"
      }
    },
    "party-uuids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/party-uuid"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "uuid",
    "title",
    "description",
    "date-time-stamp"
  ],
  "additionalProperties": false
}
```
- <a id='poam-hash'>**Hash**</a>: A representation of a cryptographic digest generated over a resource using a hash algorithm.
```json
{
  "title": "Hash",
  "description": "A representation of a cryptographic digest generated over a resource using a hash algorithm.",
  "$id": "#/definitions/hash",
  "type": "object",
  "properties": {
    "algorithm": {
      "title": "Hash algorithm",
      "description": "Method by which a hash is derived",
      "type": "string"
    },
    "value": {
      "type": "string"
    }
  },
  "required": [
    "value",
    "algorithm"
  ],
  "additionalProperties": false
}
```
- <a id='poam-implementation_statement_uuid'>**Implementation Statement UUID**</a>: Identifies the implementation statement in the SSP to which this finding is related.
```json
{
  "title": "Implementation Statement UUID",
  "description": "Identifies the implementation statement in the SSP to which this finding is related.",
  "$id": "#/definitions/implementation-statement-uuid",
  "type": "string",
  "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
}
```
- <a id='poam-implementation_status'>**Implementation Status**</a>: Identifies the implementation status of the control or control objective.
```json
{
  "title": "Implementation Status",
  "description": "Identifies the implementation status of the control or control objective.",
  "$id": "#/definitions/implementation-status",
  "type": "object",
  "properties": {
    "system": {
      "title": "Assessment System",
      "description": "Identifies the framework or rules to which this value conforms.",
      "type": "string",
      "format": "uri"
    },
    "STRVALUE": {
      "type": "string"
    }
  },
  "required": [
    "STRVALUE"
  ],
  "additionalProperties": false
}
```
- <a id='poam-implemented_component'>**Implemented Component**</a>: The set of componenets that are implemented in a given system inventory item.
```json
{
  "title": "Implemented Component",
  "description": "The set of componenets that are implemented in a given system inventory item.",
  "$id": "#/definitions/implemented-component",
  "type": "object",
  "properties": {
    "use": {
      "title": "Implementation Use Type",
      "description": "The type of implementation",
      "type": "string"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "responsible-parties": {
      "type": "object",
      "minProperties": 1,
      "additionalProperties": {
        "allOf": [
          {
            "type": "object",
            "$ref": "#/definitions/responsible-party"
          },
          {
            "not": {
              "type": "string"
            }
          }
        ]
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "additionalProperties": false
}
```
- <a id='poam-import_system_security_plan'>**Import System Security Plan**</a>: Used by the assessment plan and POA&M to import information about the system.
```json
{
  "title": "Import System Security Plan",
  "description": "Used by the assessment plan and POA&M to import information about the system.",
  "$id": "#/definitions/import-ssp",
  "type": "object",
  "properties": {
    "href": {
      "title": "hypertext reference",
      "description": "A link to a document or document fragment (actual, nominal or projected)",
      "type": "string",
      "format": "uri-reference"
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "href"
  ],
  "additionalProperties": false
}
```
- <a id='poam-inventory_item'>**Inventory Item**</a>: A single managed inventory item within the system.
```json
{
  "title": "Inventory Item",
  "description": "A single managed inventory item within the system.",
  "$id": "#/definitions/inventory-item",
  "type": "object",
  "properties": {
    "asset-id": {
      "title": "Asset Identifier",
      "description": "Organizational asset identifier that is unique in the context of the system. This may be a reference to the identifier used in an asset tracking system or a vulnerability scanning tool.",
      "type": "string"
    },
    "description": {
      "$ref": "#/definitions/description"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "responsible-parties": {
      "type": "object",
      "minProperties": 1,
      "additionalProperties": {
        "allOf": [
          {
            "type": "object",
            "$ref": "#/definitions/responsible-party"
          },
          {
            "not": {
              "type": "string"
            }
          }
        ]
      }
    },
    "implemented-components": {
      "type": "object",
      "minProperties": 1,
      "additionalProperties": {
        "allOf": [
          {
            "type": "object",
            "$ref": "#/definitions/implemented-component"
          },
          {
            "not": {
              "type": "string"
            }
          }
        ]
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "asset-id",
    "description"
  ],
  "additionalProperties": false
}
```
- <a id='poam-last_modified_timestamp'>**Last modified timestamp**</a>: Date and time of last modification.
```json
{
  "title": "Last modified timestamp",
  "description": "Date and time of last modification.",
  "$id": "#/definitions/last-modified",
  "type": "string",
  "format": "date-time",
  "pattern": "^((2000|2400|2800|(19|2[0-9](0[48]|[2468][048]|[13579][26])))-02-29)|(((19|2[0-9])[0-9]{2})-02-(0[1-9]|1[0-9]|2[0-8]))|(((19|2[0-9])[0-9]{2})-(0[13578]|10|12)-(0[1-9]|[12][0-9]|3[01]))|(((19|2[0-9])[0-9]{2})-(0[469]|11)-(0[1-9]|[12][0-9]|30))T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\\.[0-9]+)?(Z|[+-][0-9]{2}:[0-9]{2})$"
}
```
- <a id='poam-link'>**Link**</a>: A reference to a local or remote resource
```json
{
  "title": "Link",
  "description": "A reference to a local or remote resource",
  "$id": "#/definitions/link",
  "type": "object",
  "properties": {
    "href": {
      "title": "hypertext reference",
      "description": "A link to a document or document fragment (actual, nominal or projected)",
      "type": "string",
      "format": "uri-reference"
    },
    "rel": {
      "title": "Relation",
      "description": "Describes the type of relationship provided by the link. This can be an indicator of the link's purpose.",
      "type": "string"
    },
    "media-type": {
      "title": "Media type",
      "description": "Describes the media type of the linked resource",
      "type": "string"
    },
    "text": {
      "type": "string"
    }
  },
  "required": [
    "text",
    "href"
  ],
  "additionalProperties": false
}
```
- <a id='poam-local_definitions'>**Local Definitions**</a>: Allows components, and inventory-items to be defined within the POA&M for circumstances where no OSCAL-based SSP exists, or is not delivered with the POA&M.
```json
{
  "title": "Local Definitions",
  "description": "Allows components, and inventory-items to be defined within the POA&M for circumstances where no OSCAL-based SSP exists, or is not delivered with the POA&M.",
  "$id": "#/definitions/local-definitions",
  "type": "object",
  "properties": {
    "components": {
      "type": "object",
      "minProperties": 1,
      "additionalProperties": {
        "allOf": [
          {
            "type": "object",
            "$ref": "#/definitions/component"
          },
          {
            "not": {
              "type": "string"
            }
          }
        ]
      }
    },
    "inventory-items": {
      "type": "object",
      "minProperties": 1,
      "additionalProperties": {
        "allOf": [
          {
            "type": "object",
            "$ref": "#/definitions/inventory-item"
          },
          {
            "not": {
              "type": "string"
            }
          }
        ]
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "additionalProperties": false
}
```
- <a id='poam-location'>**Location**</a>: A location, with associated metadata that can be referenced.
```json
{
  "title": "Location",
  "description": "A location, with associated metadata that can be referenced.",
  "$id": "#/definitions/location",
  "type": "object",
  "properties": {
    "uuid": {
      "title": "Universally Unique Identifier",
      "description": "A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "title": {
      "$ref": "#/definitions/title"
    },
    "address": {
      "$ref": "#/definitions/address"
    },
    "email-addresses": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/email"
      }
    },
    "telephone-numbers": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/phone"
      }
    },
    "URLs": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/url"
      }
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "uuid",
    "address"
  ],
  "additionalProperties": false
}
```
- <a id='poam-location_reference'>**Location Reference**</a>: References a location defined in metadata.
```json
{
  "title": "Location Reference",
  "description": "References a location defined in metadata.",
  "$id": "#/definitions/location-uuid",
  "type": "string",
  "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
}
```
- <a id='poam-organizational_affiliation'>**Organizational Affiliation**</a>: Identifies that the containing object is a member of the organization associated with the provided UUID.
```json
{
  "title": "Organizational Affiliation",
  "description": "Identifies that the containing object is a member of the organization associated with the provided UUID.",
  "$id": "#/definitions/member-of-organization",
  "type": "string",
  "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
}
```
- <a id='poam-publication_metadata'>**Publication metadata**</a>: Provides information about the publication and availability of the containing document.
```json
{
  "title": "Publication metadata",
  "description": "Provides information about the publication and availability of the containing document.",
  "$id": "#/definitions/metadata",
  "type": "object",
  "properties": {
    "title": {
      "$ref": "#/definitions/title"
    },
    "published": {
      "$ref": "#/definitions/published"
    },
    "last-modified": {
      "$ref": "#/definitions/last-modified"
    },
    "version": {
      "$ref": "#/definitions/version"
    },
    "oscal-version": {
      "$ref": "#/definitions/oscal-version"
    },
    "revision-history": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/revision"
      }
    },
    "document-ids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/doc-id"
      }
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "roles": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/role"
      }
    },
    "locations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/location"
      }
    },
    "parties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/party"
      }
    },
    "responsible-parties": {
      "type": "object",
      "minProperties": 1,
      "additionalProperties": {
        "allOf": [
          {
            "type": "object",
            "$ref": "#/definitions/responsible-party"
          },
          {
            "not": {
              "type": "string"
            }
          }
        ]
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "title",
    "last-modified",
    "version",
    "oscal-version"
  ],
  "additionalProperties": false
}
```
- <a id='poam-mitigating_factor'>**Mitigating Factor**</a>: Describes a mitigating factor with an optional link to an implementation statement in the SSP.
```json
{
  "title": "Mitigating Factor",
  "description": "Describes a mitigating factor with an optional link to an implementation statement in the SSP.",
  "$id": "#/definitions/mitigating-factor",
  "type": "object",
  "properties": {
    "uuid": {
      "title": "Universally Unique Identifier",
      "description": "A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "implementation-uuid": {
      "title": "Implementation UUID",
      "description": "Points to an implementation statement in the SSP.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "description": {
      "$ref": "#/definitions/description"
    },
    "subject-references": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/subject-reference"
      }
    }
  },
  "required": [
    "uuid",
    "description"
  ],
  "additionalProperties": false
}
```
- <a id='poam-implementation_status'>**Implementation Status**</a>: Captures an assessors conclusions as to whether an objective is fully satisfied.
```json
{
  "title": "Implementation Status",
  "description": "Captures an assessors conclusions as to whether an objective is fully satisfied.",
  "$id": "#/definitions/objective-status",
  "type": "object",
  "properties": {
    "objective-id": {
      "title": "Objective ID",
      "description": "Points to an assessment objective.",
      "type": "string"
    },
    "control-id": {
      "title": "Control Identifier Reference",
      "description": "A reference to a control identifier.",
      "type": "string"
    },
    "title": {
      "$ref": "#/definitions/title"
    },
    "description": {
      "$ref": "#/definitions/description"
    },
    "result": {
      "$ref": "#/definitions/result"
    },
    "implementation-status": {
      "$ref": "#/definitions/implementation-status"
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "additionalProperties": false
}
```
- <a id='poam-objective'>**Objective**</a>: Describes an individual observation.
```json
{
  "title": "Objective",
  "description": "Describes an individual observation.",
  "$id": "#/definitions/observation",
  "type": "object",
  "properties": {
    "uuid": {
      "title": "Universally Unique Identifier",
      "description": "A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "title": {
      "$ref": "#/definitions/title"
    },
    "description": {
      "$ref": "#/definitions/description"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "observation-methods": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/observation-method"
      }
    },
    "observation-types": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/observation-type"
      }
    },
    "assessors": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/assessor"
      }
    },
    "subject-references": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/subject-reference"
      }
    },
    "origins": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/origin"
      }
    },
    "evidence-group": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/relevant-evidence"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "uuid",
    "description",
    "observation-methods"
  ],
  "additionalProperties": false
}
```
- <a id='poam-observation_method'>**Observation Method**</a>: Identifies how the observation was made.
```json
{
  "title": "Observation Method",
  "description": "Identifies how the observation was made.",
  "$id": "#/definitions/observation-method",
  "type": "string"
}
```
- <a id='poam-observation_type'>**Observation Type**</a>: Identifies the nature of the observation. More than one may be used to further qualify and enable filtering.
```json
{
  "title": "Observation Type",
  "description": "Identifies the nature of the observation. More than one may be used to further qualify and enable filtering.",
  "$id": "#/definitions/observation-type",
  "type": "string"
}
```
- <a id='poam-origin'>**Origin**</a>: Identifies the tool or activity that resulted in the observation.
```json
{
  "title": "Origin",
  "description": "Identifies the tool or activity that resulted in the observation.",
  "$id": "#/definitions/origin",
  "type": "object",
  "properties": {
    "uuid-ref": {
      "title": "UUID Reference",
      "description": "A pointer to a relevant item, using it's UUID.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "type": {
      "title": "Type",
      "description": "Indicating the type of identifier, address, email or other data item.",
      "type": "string",
      "enum": [
        "tool",
        "test-method",
        "task",
        "included-activity",
        "other"
      ]
    },
    "STRVALUE": {
      "type": "string"
    }
  },
  "required": [
    "STRVALUE",
    "uuid-ref",
    "type"
  ],
  "additionalProperties": false
}
```
- <a id='poam-oscal_version'>**OSCAL version**</a>: OSCAL model version.
```json
{
  "title": "OSCAL version",
  "description": "OSCAL model version.",
  "$id": "#/definitions/oscal-version",
  "type": "string"
}
```
- <a id='poam-party_(organization_or_person)'>**Party (organization or person)**</a>: A responsible entity, either singular (an organization or person) or collective (multiple persons)
```json
{
  "title": "Party (organization or person)",
  "description": "A responsible entity, either singular (an organization or person) or collective (multiple persons)",
  "$id": "#/definitions/party",
  "type": "object",
  "properties": {
    "uuid": {
      "title": "Universally Unique Identifier",
      "description": "A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "type": {
      "title": "Party Type",
      "description": "A category describing the kind of party the object describes.",
      "type": "string",
      "enum": [
        "person",
        "organization"
      ]
    },
    "party-name": {
      "$ref": "#/definitions/party-name"
    },
    "short-name": {
      "$ref": "#/definitions/short-name"
    },
    "external-ids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/external-id"
      }
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "addresses": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/address"
      }
    },
    "email-addresses": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/email"
      }
    },
    "telephone-numbers": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/phone"
      }
    },
    "member-of-organizations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/member-of-organization"
      }
    },
    "location-uuids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/location-uuid"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "uuid",
    "type",
    "party-name"
  ],
  "additionalProperties": false
}
```
- <a id='poam-party_name'>**Party Name**</a>: The full (legal) name of the party.
```json
{
  "title": "Party Name",
  "description": "The full (legal) name of the party.",
  "$id": "#/definitions/party-name",
  "type": "string"
}
```
- <a id='poam-party_reference'>**Party Reference**</a>: References a party defined in metadata.
```json
{
  "title": "Party Reference",
  "description": "References a party defined in metadata.",
  "$id": "#/definitions/party-uuid",
  "type": "string",
  "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
}
```
- <a id='poam-telephone'>**Telephone**</a>: Contact number by telephone
```json
{
  "title": "Telephone",
  "description": "Contact number by telephone",
  "$id": "#/definitions/phone",
  "type": "object",
  "properties": {
    "type": {
      "description": "Indicates the type of phone number.",
      "type": "string"
    },
    "number": {
      "type": "string"
    }
  },
  "required": [
    "number"
  ],
  "additionalProperties": false
}
```
- <a id='poam-plan_of_action_and_milestones_(poa&m)'>**Plan of Action and Milestones (POA&M)**</a>: A plan of action and milestones, such as those required by FedRAMP.
```json
{
  "title": "Plan of Action and Milestones (POA&M)",
  "description": "A plan of action and milestones, such as those required by FedRAMP.",
  "$id": "#/definitions/plan-of-action-and-milestones",
  "type": "object",
  "properties": {
    "uuid": {
      "title": "Universally Unique Identifier",
      "description": "A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "metadata": {
      "$ref": "#/definitions/metadata"
    },
    "import-ssp": {
      "$ref": "#/definitions/import-ssp"
    },
    "system-id": {
      "$ref": "#/definitions/system-id"
    },
    "local-definitions": {
      "$ref": "#/definitions/local-definitions"
    },
    "results": {
      "$ref": "#/definitions/results"
    },
    "back-matter": {
      "$ref": "#/definitions/back-matter"
    }
  },
  "required": [
    "uuid",
    "metadata",
    "results"
  ],
  "additionalProperties": false
}
```
- <a id='poam-port_range'>**Port Range**</a>: Where applicable this is the IPv4 port range on which the service operates.
```json
{
  "title": "Port Range",
  "description": "Where applicable this is the IPv4 port range on which the service operates.",
  "$id": "#/definitions/port-range",
  "type": "object",
  "properties": {
    "start": {
      "title": "Start",
      "description": "Indicates the starting port number in a port range",
      "type": "integer",
      "multipleOf": 1,
      "minimum": 0
    },
    "end": {
      "title": "End",
      "description": "Indicates the ending port number in a port range",
      "type": "integer",
      "multipleOf": 1,
      "minimum": 0
    },
    "transport": {
      "title": "Transport",
      "description": "Indicates the transport type.",
      "type": "string",
      "enum": [
        "TCP",
        "UDP"
      ]
    }
  },
  "additionalProperties": false
}
```
- <a id='poam-postal_code'>**Postal Code**</a>: Postal or ZIP code for mailing address
```json
{
  "title": "Postal Code",
  "description": "Postal or ZIP code for mailing address",
  "$id": "#/definitions/postal-code",
  "type": "string"
}
```
- <a id='poam-property'>**Property**</a>: A value with a name, attributed to the containing control, part, or group.
```json
{
  "title": "Property",
  "description": "A value with a name, attributed to the containing control, part, or group.",
  "$id": "#/definitions/prop",
  "type": "object",
  "properties": {
    "name": {
      "title": "Name",
      "description": "Identifying the purpose and intended use of the property, part or other object.",
      "type": "string"
    },
    "id": {
      "title": "Identifier",
      "description": "Unique identifier of the containing object",
      "type": "string"
    },
    "ns": {
      "title": "Namespace",
      "description": "A namespace qualifying the name.",
      "type": "string"
    },
    "class": {
      "title": "Class",
      "description": "Indicating the type or classification of the containing object",
      "type": "string"
    },
    "value": {
      "type": "string"
    }
  },
  "required": [
    "value",
    "name"
  ],
  "additionalProperties": false
}
```
- <a id='poam-protocol'>**Protocol**</a>: Information about the protocol used to provide a service.
```json
{
  "title": "Protocol",
  "description": "Information about the protocol used to provide a service.",
  "$id": "#/definitions/protocol",
  "type": "object",
  "properties": {
    "uuid": {
      "title": "Universally Unique Identifier",
      "description": "A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "name": {
      "description": "The short name of the protocol (e.g., TLS).",
      "type": "string"
    },
    "title": {
      "$ref": "#/definitions/title"
    },
    "port-ranges": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/port-range"
      }
    }
  },
  "required": [
    "name"
  ],
  "additionalProperties": false
}
```
- <a id='poam-publication_timestamp'>**Publication Timestamp**</a>: The date and time this document was published.
```json
{
  "title": "Publication Timestamp",
  "description": "The date and time this document was published.",
  "$id": "#/definitions/published",
  "type": "string",
  "format": "date-time",
  "pattern": "^((2000|2400|2800|(19|2[0-9](0[48]|[2468][048]|[13579][26])))-02-29)|(((19|2[0-9])[0-9]{2})-02-(0[1-9]|1[0-9]|2[0-8]))|(((19|2[0-9])[0-9]{2})-(0[13578]|10|12)-(0[1-9]|[12][0-9]|3[01]))|(((19|2[0-9])[0-9]{2})-(0[469]|11)-(0[1-9]|[12][0-9]|30))T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\\.[0-9]+)?(Z|[+-][0-9]{2}:[0-9]{2})$"
}
```
- <a id='poam-purpose'>**Purpose**</a>: Describes the purpose for the service within the system.
```json
{
  "title": "Purpose",
  "description": "Describes the purpose for the service within the system.",
  "$id": "#/definitions/purpose",
  "type": "string"
}
```
- <a id='poam-relevant_evidence'>**Relevant Evidence**</a>: Links this observation to relevant evidence.
```json
{
  "title": "Relevant Evidence",
  "description": "Links this observation to relevant evidence.",
  "$id": "#/definitions/relevant-evidence",
  "type": "object",
  "properties": {
    "href": {
      "description": "Links to evidence as URI. May use a URI fragment to point to a resource in the back-matter.",
      "type": "string",
      "format": "uri-reference"
    },
    "description": {
      "$ref": "#/definitions/description"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "description"
  ],
  "additionalProperties": false
}
```
- <a id='poam-remarks'>**Remarks**</a>: Additional commentary on the parent item.
```json
{
  "title": "Remarks",
  "description": "Additional commentary on the parent item.",
  "$id": "#/definitions/remarks",
  "type": "string"
}
```
- <a id='poam-remediation'>**Remediation**</a>: Describes either recommendation or an actual plan for remediating the risk.
```json
{
  "title": "Remediation",
  "description": "Describes either recommendation or an actual plan for remediating the risk.",
  "$id": "#/definitions/remediation",
  "type": "object",
  "properties": {
    "uuid": {
      "title": "Universally Unique Identifier",
      "description": "A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "type": {
      "title": "Type",
      "description": "Indicating the type of identifier, address, email or other data item.",
      "type": "string"
    },
    "title": {
      "$ref": "#/definitions/title"
    },
    "description": {
      "$ref": "#/definitions/description"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "origins": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/remediation-origin"
      }
    },
    "requirements": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/required"
      }
    },
    "schedule": {
      "$ref": "#/definitions/schedule"
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "uuid",
    "title",
    "description"
  ],
  "additionalProperties": false
}
```
- <a id='poam-remediation_origin'>**Remediation Origin**</a>: Points to the source of the remediation recommendation or plan
```json
{
  "title": "Remediation Origin",
  "description": "Points to the source of the remediation recommendation or plan",
  "$id": "#/definitions/remediation-origin",
  "type": "object",
  "properties": {
    "uuid-ref": {
      "title": "UUID Reference",
      "description": "A pointer to a relevant item, using it's UUID.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "type": {
      "title": "Type",
      "description": "Indicating the type of identifier, address, email or other data item.",
      "type": "string"
    },
    "STRVALUE": {
      "type": "string"
    }
  },
  "required": [
    "STRVALUE",
    "uuid-ref"
  ],
  "additionalProperties": false
}
```
- <a id='poam-remediation_tracking'>**Remediation Tracking**</a>: A log of events and actions taken towards the remediation of the associated risk.
```json
{
  "title": "Remediation Tracking",
  "description": "A log of events and actions taken towards the remediation of the associated risk.",
  "$id": "#/definitions/remediation-tracking",
  "type": "object",
  "properties": {
    "tracking-entries": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/tracking-entry"
      }
    }
  },
  "required": [
    "tracking-entries"
  ],
  "additionalProperties": false
}
```
- <a id='poam-required'>**Required**</a>: Identifies something required to achieve remediation.
```json
{
  "title": "Required",
  "description": "Identifies something required to achieve remediation.",
  "$id": "#/definitions/required",
  "type": "object",
  "properties": {
    "uuid": {
      "title": "Universally Unique Identifier",
      "description": "A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "subject-references": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/subject-reference"
      }
    },
    "title": {
      "$ref": "#/definitions/title"
    },
    "description": {
      "$ref": "#/definitions/description"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "uuid",
    "description"
  ],
  "additionalProperties": false
}
```
- <a id='poam-resource'>**Resource**</a>: A resource associated with the present document, which may be a pointer to other data or a citation.
```json
{
  "title": "Resource",
  "description": "A resource associated with the present document, which may be a pointer to other data or a citation.",
  "$id": "#/definitions/resource",
  "type": "object",
  "properties": {
    "uuid": {
      "title": "Universally Unique Identifier",
      "description": "A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "title": {
      "$ref": "#/definitions/title"
    },
    "desc": {
      "$ref": "#/definitions/desc"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "document-ids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/doc-id"
      }
    },
    "citation": {
      "$ref": "#/definitions/citation"
    },
    "rlinks": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/rlink"
      }
    },
    "attachments": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/base64"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "uuid"
  ],
  "additionalProperties": false
}
```
- <a id='poam-responsible_party'>**Responsible Party**</a>: A reference to a set of organizations or persons that have responsibility for performing a referenced role relative to the parent context.
```json
{
  "title": "Responsible Party",
  "description": "A reference to a set of organizations or persons that have responsibility for performing a referenced role relative to the parent context.",
  "$id": "#/definitions/responsible-party",
  "type": "object",
  "properties": {
    "party-uuids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/party-uuid"
      }
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "party-uuids"
  ],
  "additionalProperties": false
}
```
- <a id='poam-responsible_role'>**Responsible Role**</a>: A reference to one or more roles with responsibility for performing a function relative to the control.
```json
{
  "title": "Responsible Role",
  "description": "A reference to one or more roles with responsibility for performing a function relative to the control.",
  "$id": "#/definitions/responsible-role",
  "type": "object",
  "properties": {
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "party-ids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/party-uuid"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "additionalProperties": false
}
```
- <a id='poam-result'>**Result**</a>: A brief indication as to whether the objective is satisfied or not.
```json
{
  "title": "Result",
  "description": "A brief indication as to whether the objective is satisfied or not.",
  "$id": "#/definitions/result",
  "type": "object",
  "properties": {
    "system": {
      "title": "Assessment System",
      "description": "Identifies the framework or rules to which this value conforms.",
      "type": "string",
      "format": "uri"
    },
    "STRVALUE": {
      "type": "string"
    }
  },
  "required": [
    "STRVALUE"
  ],
  "additionalProperties": false
}
```
- <a id='poam-assessment_results'>**Assessment Results**</a>: Used by the assessment results and POA&M. In the assessment results, this identifies all of the assessment observations and findings, initial and residual risks, deviations, and disposition. In the POA&M, this identifies initial and residual risks, deviations, and disposition.
```json
{
  "title": "Assessment Results",
  "description": "Used by the assessment results and POA&M. In the assessment results, this identifies all of the assessment observations and findings, initial and residual risks, deviations, and disposition. In the POA&M, this identifies initial and residual risks, deviations, and disposition.",
  "$id": "#/definitions/results",
  "type": "object",
  "properties": {
    "uuid": {
      "title": "Universally Unique Identifier",
      "description": "A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "title": {
      "$ref": "#/definitions/title"
    },
    "description": {
      "$ref": "#/definitions/description"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "start": {
      "$ref": "#/definitions/start"
    },
    "end": {
      "$ref": "#/definitions/end"
    },
    "findings": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/finding"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "uuid",
    "title",
    "description",
    "start",
    "end",
    "findings"
  ],
  "additionalProperties": false
}
```
- <a id='poam-revision_history_entry'>**Revision History Entry**</a>: An entry in a sequential list of revisions to the containing document in reverse chronological order (i.e., most recent previous revision first).
```json
{
  "title": "Revision History Entry",
  "description": "An entry in a sequential list of revisions to the containing document in reverse chronological order (i.e., most recent previous revision first).",
  "$id": "#/definitions/revision",
  "type": "object",
  "properties": {
    "title": {
      "$ref": "#/definitions/title"
    },
    "published": {
      "$ref": "#/definitions/published"
    },
    "last-modified": {
      "$ref": "#/definitions/last-modified"
    },
    "version": {
      "$ref": "#/definitions/version"
    },
    "oscal-version": {
      "$ref": "#/definitions/oscal-version"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "additionalProperties": false
}
```
- <a id='poam-identified_risk'>**Identified Risk**</a>: An identified risk.
```json
{
  "title": "Identified Risk",
  "description": "An identified risk.",
  "$id": "#/definitions/risk",
  "type": "object",
  "properties": {
    "uuid": {
      "title": "Universally Unique Identifier",
      "description": "A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "title": {
      "$ref": "#/definitions/title"
    },
    "description": {
      "$ref": "#/definitions/description"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "risk-metrics": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/risk-metric"
      }
    },
    "risk-statement": {
      "$ref": "#/definitions/risk-statement"
    },
    "mitigating-factors": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/mitigating-factor"
      }
    },
    "remediation-group": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/remediation"
      }
    },
    "risk-status": {
      "$ref": "#/definitions/risk-status"
    },
    "closure-actions": {
      "$ref": "#/definitions/closure-actions"
    },
    "remediation-tracking": {
      "$ref": "#/definitions/remediation-tracking"
    },
    "party-uuids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/party-uuid"
      }
    }
  },
  "required": [
    "uuid",
    "title",
    "description",
    "risk-statement",
    "risk-status"
  ],
  "additionalProperties": false
}
```
- <a id='poam-risk_metric'>**Risk Metric**</a>: An individual risk metric from a specified system.
```json
{
  "title": "Risk Metric",
  "description": "An individual risk metric from a specified system.",
  "$id": "#/definitions/risk-metric",
  "type": "object",
  "properties": {
    "name": {
      "title": "Name",
      "description": "Identifying the purpose and intended use of the property, part or other object.",
      "type": "string"
    },
    "class": {
      "title": "Class",
      "description": "Indicating the type or classification of the containing object",
      "type": "string"
    },
    "system": {
      "title": "System",
      "description": "Specifies the system represented by this risk metric.",
      "type": "string"
    },
    "STRVALUE": {
      "type": "string"
    }
  },
  "required": [
    "STRVALUE",
    "name"
  ],
  "additionalProperties": false
}
```
- <a id='poam-risk_statement'>**Risk Statement**</a>: Describes the risk.
```json
{
  "title": "Risk Statement",
  "description": "Describes the risk.",
  "$id": "#/definitions/risk-statement",
  "type": "string"
}
```
- <a id='poam-status'>**Status**</a>: Describes the status of the associated risk.
```json
{
  "title": "Status",
  "description": "Describes the status of the associated risk.",
  "$id": "#/definitions/risk-status",
  "type": "string"
}
```
- <a id='poam-resource_link'>**Resource link**</a>: A pointer to an external copy of a document with optional hash for verification
```json
{
  "title": "Resource link",
  "description": "A pointer to an external copy of a document with optional hash for verification",
  "$id": "#/definitions/rlink",
  "type": "object",
  "properties": {
    "href": {
      "title": "hypertext reference",
      "description": "A link to a document or document fragment (actual, nominal or projected)",
      "type": "string",
      "format": "uri-reference"
    },
    "media-type": {
      "title": "Media type",
      "description": "Describes the media type of the linked resource",
      "type": "string"
    },
    "hashes": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/hash"
      }
    }
  },
  "required": [
    "href"
  ],
  "additionalProperties": false
}
```
- <a id='poam-role'>**Role**</a>: Defining a role to be assigned to a party
```json
{
  "title": "Role",
  "description": "Defining a role to be assigned to a party",
  "$id": "#/definitions/role",
  "type": "object",
  "properties": {
    "id": {
      "title": "Identifier",
      "description": "Unique identifier of the containing object",
      "type": "string"
    },
    "title": {
      "$ref": "#/definitions/title"
    },
    "short-name": {
      "$ref": "#/definitions/short-name"
    },
    "desc": {
      "$ref": "#/definitions/desc"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "id",
    "title"
  ],
  "additionalProperties": false
}
```
- <a id='poam-role_identifier_reference'>**Role Identifier Reference**</a>: A reference to the roles served by the user.
```json
{
  "title": "Role Identifier Reference",
  "description": "A reference to the roles served by the user.",
  "$id": "#/definitions/role-id",
  "type": "string"
}
```
- <a id='poam-schedule'>**Schedule**</a>: Identifies the schedule for the assessment activities.
```json
{
  "title": "Schedule",
  "description": "Identifies the schedule for the assessment activities.",
  "$id": "#/definitions/schedule",
  "type": "object",
  "properties": {
    "uuid": {
      "title": "Universally Unique Identifier",
      "description": "A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "tasks": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/task"
      }
    }
  },
  "required": [
    "tasks"
  ],
  "additionalProperties": false
}
```
- <a id='poam-short-name'>**short-name**</a>: A common name, short name or acronym
```json
{
  "title": "short-name",
  "description": "A common name, short name or acronym",
  "$id": "#/definitions/short-name",
  "type": "string"
}
```
- <a id='poam-start'>**Start**</a>: Identifies the start of a task.
```json
{
  "title": "Start",
  "description": "Identifies the start of a task.",
  "$id": "#/definitions/start",
  "type": "string",
  "format": "date-time",
  "pattern": "^((2000|2400|2800|(19|2[0-9](0[48]|[2468][048]|[13579][26])))-02-29)|(((19|2[0-9])[0-9]{2})-02-(0[1-9]|1[0-9]|2[0-8]))|(((19|2[0-9])[0-9]{2})-(0[13578]|10|12)-(0[1-9]|[12][0-9]|3[01]))|(((19|2[0-9])[0-9]{2})-(0[469]|11)-(0[1-9]|[12][0-9]|30))T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\\.[0-9]+)?(Z|[+-][0-9]{2}:[0-9]{2})$"
}
```
- <a id='poam-state'>**State**</a>: State, province or analogous geographical region for mailing address
```json
{
  "title": "State",
  "description": "State, province or analogous geographical region for mailing address",
  "$id": "#/definitions/state",
  "type": "string"
}
```
- <a id='poam-status'>**Status**</a>: Describes the operational status of the system.
```json
{
  "title": "Status",
  "description": "Describes the operational status of the system.",
  "$id": "#/definitions/status",
  "type": "object",
  "properties": {
    "state": {
      "title": "State",
      "description": "The current operating status.",
      "type": "string",
      "enum": [
        "operational",
        "under-development",
        "under-major-modification",
        "disposition",
        "other"
      ]
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "state"
  ],
  "additionalProperties": false
}
```
- <a id='poam-identifies_the_subject'>**Identifies the Subject**</a>: A pointer to a resource based on its ID. Use type to indicate whether the identified resource is a component, inventory item, location, user, or something else.
```json
{
  "title": "Identifies the Subject",
  "description": "A pointer to a resource based on its ID. Use type to indicate whether the identified resource is a component, inventory item, location, user, or something else.",
  "$id": "#/definitions/subject-reference",
  "type": "object",
  "properties": {
    "uuid-ref": {
      "title": "UUID Reference",
      "description": "A pointer to a component, inventory-item, location, party, user, or resource using it's UUID.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "type": {
      "title": "Type",
      "description": "Indicating the type of identifier, address, email or other data item.",
      "type": "string"
    },
    "title": {
      "$ref": "#/definitions/title"
    },
    "props": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    }
  },
  "required": [
    "uuid-ref",
    "type"
  ],
  "additionalProperties": false
}
```
- <a id='poam-system_identification'>**System Identification**</a>: A unique identifier for the system described by this system security plan.
```json
{
  "title": "System Identification",
  "description": "A unique identifier for the system described by this system security plan.",
  "$id": "#/definitions/system-id",
  "type": "object",
  "properties": {
    "identifier-type": {
      "title": "Identification System Type",
      "description": "Identifies the identification system from which the provided identifier was assigned.",
      "type": "string",
      "format": "uri"
    },
    "id": {
      "type": "string"
    }
  },
  "required": [
    "id"
  ],
  "additionalProperties": false
}
```
- <a id='poam-task'>**Task**</a>: Identifies an individual task.
```json
{
  "title": "Task",
  "description": "Identifies an individual task.",
  "$id": "#/definitions/task",
  "type": "object",
  "properties": {
    "uuid": {
      "title": "Universally Unique Identifier",
      "description": "A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "title": {
      "$ref": "#/definitions/title"
    },
    "description": {
      "$ref": "#/definitions/description"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "start": {
      "$ref": "#/definitions/start"
    },
    "end": {
      "$ref": "#/definitions/end"
    },
    "activity-uuids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/activity-uuid"
      }
    },
    "role-ids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/role-id"
      }
    },
    "party-uuids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/party-uuid"
      }
    },
    "location-uuids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/location-uuid"
      }
    },
    "compare-to": {
      "$ref": "#/definitions/compare-to"
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "uuid"
  ],
  "additionalProperties": false
}
```
- <a id='poam-text'>**Text**</a>: A line of textual content whose semantic is determined by the context of use.
```json
{
  "title": "Text",
  "description": "A line of textual content whose semantic is determined by the context of use.",
  "$id": "#/definitions/text",
  "type": "string"
}
```
- <a id='poam-threat_id'>**Threat ID**</a>: A pointer, by ID, to an externally-defined threat.
```json
{
  "title": "Threat ID",
  "description": "A pointer, by ID, to an externally-defined threat.",
  "$id": "#/definitions/threat-id",
  "type": "object",
  "properties": {
    "system": {
      "title": "Threat Type Identification System",
      "description": "Specifies the source of the threat information.",
      "type": "string",
      "format": "uri"
    },
    "uri": {
      "title": "URI",
      "description": "An optional location for the threat data, from which this ID originates.",
      "type": "string",
      "format": "uri"
    },
    "STRVALUE": {
      "type": "string"
    }
  },
  "required": [
    "STRVALUE",
    "system"
  ],
  "additionalProperties": false
}
```
- <a id='poam-title'>**Title**</a>: A title for display and navigation
```json
{
  "title": "Title",
  "description": "A title for display and navigation",
  "$id": "#/definitions/title",
  "type": "string"
}
```
- <a id='poam-tracking_entry'>**Tracking Entry**</a>: Individual remediation tracking entry, which logs an event or action taken towards the remediation of the associated risk.
```json
{
  "title": "Tracking Entry",
  "description": "Individual remediation tracking entry, which logs an event or action taken towards the remediation of the associated risk.",
  "$id": "#/definitions/tracking-entry",
  "type": "object",
  "properties": {
    "uuid": {
      "title": "Universally Unique Identifier",
      "description": "A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "type": {
      "title": "Type",
      "description": "Indicating the type of identifier, address, email or other data item.",
      "type": "string"
    },
    "date-time-stamp": {
      "$ref": "#/definitions/date-time-stamp"
    },
    "title": {
      "$ref": "#/definitions/title"
    },
    "description": {
      "$ref": "#/definitions/description"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "uuid",
    "date-time-stamp",
    "description"
  ],
  "additionalProperties": false
}
```
- <a id='poam-url'>**URL**</a>: URL for web site or Internet presence
```json
{
  "title": "URL",
  "description": "URL for web site or Internet presence",
  "$id": "#/definitions/url",
  "type": "string",
  "format": "uri"
}
```
- <a id='poam-document_version'>**Document version**</a>: The version of the document content.
```json
{
  "title": "Document version",
  "description": "The version of the document content.",
  "$id": "#/definitions/version",
  "type": "string"
}
```

## profile

> OSCAL Profile Metaschema

- <a id='profile-addition'>**Addition**</a>: Specifies contents to be added into controls, in resolution
```json
{
  "title": "Addition",
  "description": "Specifies contents to be added into controls, in resolution",
  "$id": "#/definitions/add",
  "type": "object",
  "properties": {
    "position": {
      "title": "Position",
      "description": "Where to add the new content with respect to the targeted element (beside it or inside it)",
      "type": "string",
      "enum": [
        "before",
        "after",
        "starting",
        "ending"
      ]
    },
    "id-ref": {
      "title": "Reference by ID",
      "description": "Target location of the addition.",
      "type": "string"
    },
    "title": {
      "$ref": "#/definitions/title"
    },
    "parameters": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/param"
      }
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "parts": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/part"
      }
    }
  },
  "additionalProperties": false
}
```
- <a id='profile-address_line'>**Address line**</a>: A single line of an address.
```json
{
  "title": "Address line",
  "description": "A single line of an address.",
  "$id": "#/definitions/addr-line",
  "type": "string"
}
```
- <a id='profile-address'>**Address**</a>: A postal address.
```json
{
  "title": "Address",
  "description": "A postal address.",
  "$id": "#/definitions/address",
  "type": "object",
  "properties": {
    "type": {
      "description": "Indicates the type of address.",
      "type": "string"
    },
    "postal-address": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/addr-line"
      }
    },
    "city": {
      "$ref": "#/definitions/city"
    },
    "state": {
      "$ref": "#/definitions/state"
    },
    "postal-code": {
      "$ref": "#/definitions/postal-code"
    },
    "country": {
      "$ref": "#/definitions/country"
    }
  },
  "additionalProperties": false
}
```
- <a id='profile-include_all'>**Include all**</a>: Include all controls from the imported resource (catalog)
```json
{
  "title": "Include all",
  "description": "Include all controls from the imported resource (catalog)",
  "$id": "#/definitions/all",
  "type": "object",
  "properties": {
    "with-child-controls": {
      "title": "Include contained controls with control",
      "description": "When a control is included, whether its child (dependent) controls are also included.",
      "type": "string",
      "enum": [
        "yes",
        "no"
      ]
    }
  },
  "additionalProperties": false
}
```
- <a id='profile-alteration'>**Alteration**</a>: An Alter element specifies changes to be made to an included control when a profile is resolved.
```json
{
  "title": "Alteration",
  "description": "An Alter element specifies changes to be made to an included control when a profile is resolved.",
  "$id": "#/definitions/alter",
  "type": "object",
  "properties": {
    "control-id": {
      "title": "Control ID",
      "description": "Value of the 'id' flag on a target control",
      "type": "string"
    },
    "removals": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/remove"
      }
    },
    "additions": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/add"
      }
    }
  },
  "additionalProperties": false
}
```
- <a id='profile-annotation'>**Annotation**</a>: A name/value pair with optional explanatory remarks.
```json
{
  "title": "Annotation",
  "description": "A name/value pair with optional explanatory remarks.",
  "$id": "#/definitions/annotation",
  "type": "object",
  "properties": {
    "name": {
      "title": "Name",
      "description": "Identifying the purpose and intended use of the property, part or other object.",
      "type": "string"
    },
    "id": {
      "title": "Identifier",
      "description": "Unique identifier of the containing object",
      "type": "string"
    },
    "ns": {
      "title": "Namespace",
      "description": "A namespace qualifying the name.",
      "type": "string"
    },
    "value": {
      "title": "Value",
      "description": "Indicates the value of the characteristic.",
      "type": "string"
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "name"
  ],
  "additionalProperties": false
}
```
- <a id='profile-as_is'>**As is**</a>: An As-is element indicates that the controls should be structured in resolution as they are structured in their source catalogs. It does not contain any elements or attributes.
```json
{
  "title": "As is",
  "description": "An As-is element indicates that the controls should be structured in resolution as they are structured in their source catalogs. It does not contain any elements or attributes.",
  "$id": "#/definitions/as-is",
  "type": "boolean"
}
```
- <a id='profile-back_matter'>**Back matter**</a>: A collection of citations and resource references.
```json
{
  "title": "Back matter",
  "description": "A collection of citations and resource references.",
  "$id": "#/definitions/back-matter",
  "type": "object",
  "properties": {
    "resources": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/resource"
      }
    }
  },
  "additionalProperties": false
}
```
- <a id='profile-base64'>**Base64**</a>: 
```json
{
  "title": "Base64",
  "description": "",
  "$id": "#/definitions/base64",
  "type": "object",
  "properties": {
    "filename": {
      "title": "File Name",
      "description": "Name of the file before it was encoded as Base64 to be embedded in a resource. This is the name that will be assigned to the file when the file is decoded.",
      "type": "string",
      "format": "uri-reference"
    },
    "media-type": {
      "title": "Media type",
      "description": "Describes the media type of the linked resource",
      "type": "string"
    },
    "value": {
      "type": "string"
    }
  },
  "required": [
    "value"
  ],
  "additionalProperties": false
}
```
- <a id='profile-bibliographic_definition'>**Bibliographic Definition**</a>: A container in which a set of bibliographic information can included. The model of this information is undefined by OSCAL.
```json
{
  "title": "Bibliographic Definition",
  "description": "A container in which a set of bibliographic information can included. The model of this information is undefined by OSCAL.",
  "$id": "#/definitions/biblio",
  "type": "object",
  "additionalProperties": false
}
```
- <a id='profile-call'>**Call**</a>: Call a control by its ID
```json
{
  "title": "Call",
  "description": "Call a control by its ID",
  "$id": "#/definitions/call",
  "type": "object",
  "properties": {
    "control-id": {
      "title": "Control ID",
      "description": "Value of the 'id' flag on a target control",
      "type": "string"
    },
    "with-child-controls": {
      "title": "Include contained controls with control",
      "description": "When a control is included, whether its child (dependent) controls are also included.",
      "type": "string",
      "enum": [
        "yes",
        "no"
      ]
    }
  },
  "required": [
    "control-id"
  ],
  "additionalProperties": false
}
```
- <a id='profile-choice'>**Choice**</a>: A value selection among several such options
```json
{
  "title": "Choice",
  "description": "A value selection among several such options",
  "$id": "#/definitions/choice",
  "type": "string"
}
```
- <a id='profile-citation'>**Citation**</a>: A citation consisting of end note text and optional structured bibliographic data.
```json
{
  "title": "Citation",
  "description": "A citation consisting of end note text and optional structured bibliographic data.",
  "$id": "#/definitions/citation",
  "type": "object",
  "properties": {
    "text": {
      "$ref": "#/definitions/text"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "biblio": {
      "$ref": "#/definitions/biblio"
    }
  },
  "required": [
    "text"
  ],
  "additionalProperties": false
}
```
- <a id='profile-city'>**City**</a>: City, town or geographical region for mailing address
```json
{
  "title": "City",
  "description": "City, town or geographical region for mailing address",
  "$id": "#/definitions/city",
  "type": "string"
}
```
- <a id='profile-combination_rule'>**Combination rule**</a>: A Combine element defines whether and how to combine multiple (competing) versions of the same control
```json
{
  "title": "Combination rule",
  "description": "A Combine element defines whether and how to combine multiple (competing) versions of the same control",
  "$id": "#/definitions/combine",
  "type": "object",
  "properties": {
    "method": {
      "title": "Combination method",
      "description": "How clashing controls should be handled",
      "type": "string",
      "enum": [
        "use-first",
        "merge",
        "keep"
      ]
    }
  },
  "additionalProperties": false
}
```
- <a id='profile-constraint'>**Constraint**</a>: A formal or informal expression of a constraint or test
```json
{
  "title": "Constraint",
  "description": "A formal or informal expression of a constraint or test",
  "$id": "#/definitions/constraint",
  "type": "object",
  "properties": {
    "test": {
      "title": "Constraint test",
      "description": "A formal (executable) expression of a constraint",
      "type": "string"
    },
    "detail": {
      "type": "string"
    }
  },
  "required": [
    "detail"
  ],
  "additionalProperties": false
}
```
- <a id='profile-country'>**Country**</a>: Country for mailing address
```json
{
  "title": "Country",
  "description": "Country for mailing address",
  "$id": "#/definitions/country",
  "type": "string"
}
```
- <a id='profile-custom_grouping'>**Custom grouping**</a>: A Custom element frames a structure for embedding represented controls in resolution.
```json
{
  "title": "Custom grouping",
  "description": "A Custom element frames a structure for embedding represented controls in resolution.",
  "$id": "#/definitions/custom",
  "type": "object",
  "properties": {
    "groups": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/group"
      }
    },
    "id-selectors": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/call"
      }
    },
    "pattern-selectors": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/match"
      }
    }
  },
  "additionalProperties": false
}
```
- <a id='profile-description'>**Description**</a>: A short textual description
```json
{
  "title": "Description",
  "description": "A short textual description",
  "$id": "#/definitions/desc",
  "type": "string"
}
```
- <a id='profile-document_identifier'>**Document Identifier**</a>: A document identifier qualified by an identifier type.
```json
{
  "title": "Document Identifier",
  "description": "A document identifier qualified by an identifier type.",
  "$id": "#/definitions/doc-id",
  "type": "object",
  "properties": {
    "type": {
      "description": "Qualifies the kind of document identifier.",
      "type": "string"
    },
    "identifier": {
      "type": "string"
    }
  },
  "required": [
    "identifier",
    "type"
  ],
  "additionalProperties": false
}
```
- <a id='profile-email'>**Email**</a>: Email address
```json
{
  "title": "Email",
  "description": "Email address",
  "$id": "#/definitions/email",
  "type": "string",
  "format": "email",
  "pattern": "^.+@.+"
}
```
- <a id='profile-exclude_controls'>**Exclude controls**</a>: Which controls to exclude from the resource (source catalog) being imported
```json
{
  "title": "Exclude controls",
  "description": "Which controls to exclude from the resource (source catalog) being imported",
  "$id": "#/definitions/exclude",
  "type": "object",
  "properties": {
    "id-selectors": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/call"
      }
    },
    "pattern-selectors": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/match"
      }
    }
  },
  "additionalProperties": false
}
```
- <a id='profile-personal_identifier'>**Personal Identifier**</a>: An identifier for a person (such as an ORCID) using a designated scheme.
```json
{
  "title": "Personal Identifier",
  "description": "An identifier for a person (such as an ORCID) using a designated scheme.",
  "$id": "#/definitions/external-id",
  "type": "object",
  "properties": {
    "type": {
      "title": "Type",
      "description": "Indicating the type of identifier, address, email or other data item.",
      "type": "string"
    },
    "id": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "type"
  ],
  "additionalProperties": false
}
```
- <a id='profile-control_group'>**Control group**</a>: As in catalogs, a group of (selected) controls or of groups of controls
```json
{
  "title": "Control group",
  "description": "As in catalogs, a group of (selected) controls or of groups of controls",
  "$id": "#/definitions/group",
  "type": "object",
  "properties": {
    "id": {
      "title": "Identifier",
      "description": "Unique identifier of the containing object",
      "type": "string"
    },
    "class": {
      "title": "Class",
      "description": "Indicating the type or classification of the containing object",
      "type": "string"
    },
    "title": {
      "$ref": "#/definitions/title"
    },
    "parameters": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/param"
      }
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "parts": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/part"
      }
    },
    "groups": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/group"
      }
    },
    "id-selectors": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/call"
      }
    },
    "pattern-selectors": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/match"
      }
    }
  },
  "additionalProperties": false
}
```
- <a id='profile-guideline'>**Guideline**</a>: A prose statement that provides a recommendation for the use of a parameter.
```json
{
  "title": "Guideline",
  "description": "A prose statement that provides a recommendation for the use of a parameter.",
  "$id": "#/definitions/guideline",
  "type": "object",
  "properties": {
    "prose": {
      "$ref": "#/definitions/prose"
    }
  },
  "additionalProperties": false
}
```
- <a id='profile-hash'>**Hash**</a>: A representation of a cryptographic digest generated over a resource using a hash algorithm.
```json
{
  "title": "Hash",
  "description": "A representation of a cryptographic digest generated over a resource using a hash algorithm.",
  "$id": "#/definitions/hash",
  "type": "object",
  "properties": {
    "algorithm": {
      "title": "Hash algorithm",
      "description": "Method by which a hash is derived",
      "type": "string"
    },
    "value": {
      "type": "string"
    }
  },
  "required": [
    "value",
    "algorithm"
  ],
  "additionalProperties": false
}
```
- <a id='profile-import_resource'>**Import resource**</a>: An Import element designates a catalog, profile, or other resource to be included (referenced and potentially modified) by this profile.
```json
{
  "title": "Import resource",
  "description": "An Import element designates a catalog, profile, or other resource to be included (referenced and potentially modified) by this profile.",
  "$id": "#/definitions/import",
  "type": "object",
  "properties": {
    "href": {
      "title": "hypertext reference",
      "description": "A link to a document or document fragment (actual, nominal or projected)",
      "type": "string",
      "format": "uri-reference"
    },
    "include": {
      "$ref": "#/definitions/include"
    },
    "exclude": {
      "$ref": "#/definitions/exclude"
    }
  },
  "required": [
    "href"
  ],
  "additionalProperties": false
}
```
- <a id='profile-include_controls'>**Include controls**</a>: Specifies which controls to include from the resource (source catalog) being imported
```json
{
  "title": "Include controls",
  "description": "Specifies which controls to include from the resource (source catalog) being imported",
  "$id": "#/definitions/include",
  "type": "object",
  "properties": {
    "all": {
      "$ref": "#/definitions/all"
    },
    "id-selectors": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/call"
      }
    },
    "pattern-selectors": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/match"
      }
    }
  },
  "additionalProperties": false
}
```
- <a id='profile-parameter_label'>**Parameter label**</a>: A placeholder for a missing value, in display.
```json
{
  "title": "Parameter label",
  "description": "A placeholder for a missing value, in display.",
  "$id": "#/definitions/label",
  "type": "string"
}
```
- <a id='profile-last_modified_timestamp'>**Last modified timestamp**</a>: Date and time of last modification.
```json
{
  "title": "Last modified timestamp",
  "description": "Date and time of last modification.",
  "$id": "#/definitions/last-modified",
  "type": "string",
  "format": "date-time",
  "pattern": "^((2000|2400|2800|(19|2[0-9](0[48]|[2468][048]|[13579][26])))-02-29)|(((19|2[0-9])[0-9]{2})-02-(0[1-9]|1[0-9]|2[0-8]))|(((19|2[0-9])[0-9]{2})-(0[13578]|10|12)-(0[1-9]|[12][0-9]|3[01]))|(((19|2[0-9])[0-9]{2})-(0[469]|11)-(0[1-9]|[12][0-9]|30))T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\\.[0-9]+)?(Z|[+-][0-9]{2}:[0-9]{2})$"
}
```
- <a id='profile-link'>**Link**</a>: A reference to a local or remote resource
```json
{
  "title": "Link",
  "description": "A reference to a local or remote resource",
  "$id": "#/definitions/link",
  "type": "object",
  "properties": {
    "href": {
      "title": "hypertext reference",
      "description": "A link to a document or document fragment (actual, nominal or projected)",
      "type": "string",
      "format": "uri-reference"
    },
    "rel": {
      "title": "Relation",
      "description": "Describes the type of relationship provided by the link. This can be an indicator of the link's purpose.",
      "type": "string"
    },
    "media-type": {
      "title": "Media type",
      "description": "Describes the media type of the linked resource",
      "type": "string"
    },
    "text": {
      "type": "string"
    }
  },
  "required": [
    "text",
    "href"
  ],
  "additionalProperties": false
}
```
- <a id='profile-location'>**Location**</a>: A location, with associated metadata that can be referenced.
```json
{
  "title": "Location",
  "description": "A location, with associated metadata that can be referenced.",
  "$id": "#/definitions/location",
  "type": "object",
  "properties": {
    "uuid": {
      "title": "Universally Unique Identifier",
      "description": "A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "title": {
      "$ref": "#/definitions/title"
    },
    "address": {
      "$ref": "#/definitions/address"
    },
    "email-addresses": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/email"
      }
    },
    "telephone-numbers": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/phone"
      }
    },
    "URLs": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/url"
      }
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "uuid",
    "address"
  ],
  "additionalProperties": false
}
```
- <a id='profile-location_reference'>**Location Reference**</a>: References a location defined in metadata.
```json
{
  "title": "Location Reference",
  "description": "References a location defined in metadata.",
  "$id": "#/definitions/location-uuid",
  "type": "string",
  "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
}
```
- <a id='profile-match_controls_by_identifier'>**Match controls by identifier**</a>: Select controls by (regular expression) match on ID
```json
{
  "title": "Match controls by identifier",
  "description": "Select controls by (regular expression) match on ID",
  "$id": "#/definitions/match",
  "type": "object",
  "properties": {
    "pattern": {
      "title": "Pattern",
      "description": "A regular expression matching the IDs of one or more controls to be selected",
      "type": "string"
    },
    "order": {
      "title": "Order",
      "description": "A designation of how a selection of controls in a profile is to be ordered.",
      "type": "string",
      "enum": [
        "keep",
        "ascending",
        "descending"
      ]
    },
    "with-child-controls": {
      "title": "Include contained controls with control",
      "description": "When a control is included, whether its child (dependent) controls are also included.",
      "type": "string",
      "enum": [
        "yes",
        "no"
      ]
    }
  },
  "additionalProperties": false
}
```
- <a id='profile-organizational_affiliation'>**Organizational Affiliation**</a>: Identifies that the containing object is a member of the organization associated with the provided UUID.
```json
{
  "title": "Organizational Affiliation",
  "description": "Identifies that the containing object is a member of the organization associated with the provided UUID.",
  "$id": "#/definitions/member-of-organization",
  "type": "string",
  "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
}
```
- <a id='profile-merge_controls'>**Merge controls**</a>: A Merge element merges controls in resolution.
```json
{
  "title": "Merge controls",
  "description": "A Merge element merges controls in resolution.",
  "$id": "#/definitions/merge",
  "type": "object",
  "properties": {
    "combine": {
      "$ref": "#/definitions/combine"
    },
    "as-is": {
      "$ref": "#/definitions/as-is"
    },
    "custom": {
      "$ref": "#/definitions/custom"
    }
  },
  "additionalProperties": false
}
```
- <a id='profile-publication_metadata'>**Publication metadata**</a>: Provides information about the publication and availability of the containing document.
```json
{
  "title": "Publication metadata",
  "description": "Provides information about the publication and availability of the containing document.",
  "$id": "#/definitions/metadata",
  "type": "object",
  "properties": {
    "title": {
      "$ref": "#/definitions/title"
    },
    "published": {
      "$ref": "#/definitions/published"
    },
    "last-modified": {
      "$ref": "#/definitions/last-modified"
    },
    "version": {
      "$ref": "#/definitions/version"
    },
    "oscal-version": {
      "$ref": "#/definitions/oscal-version"
    },
    "revision-history": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/revision"
      }
    },
    "document-ids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/doc-id"
      }
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "roles": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/role"
      }
    },
    "locations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/location"
      }
    },
    "parties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/party"
      }
    },
    "responsible-parties": {
      "type": "object",
      "minProperties": 1,
      "additionalProperties": {
        "allOf": [
          {
            "type": "object",
            "$ref": "#/definitions/responsible-party"
          },
          {
            "not": {
              "type": "string"
            }
          }
        ]
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "title",
    "last-modified",
    "version",
    "oscal-version"
  ],
  "additionalProperties": false
}
```
- <a id='profile-modify_controls'>**Modify controls**</a>: Set parameters or amend controls in resolution
```json
{
  "title": "Modify controls",
  "description": "Set parameters or amend controls in resolution",
  "$id": "#/definitions/modify",
  "type": "object",
  "properties": {
    "parameter-settings": {
      "type": "object",
      "minProperties": 1,
      "additionalProperties": {
        "allOf": [
          {
            "type": "object",
            "$ref": "#/definitions/set-parameter"
          },
          {
            "not": {
              "type": "string"
            }
          }
        ]
      }
    },
    "alterations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/alter"
      }
    }
  },
  "additionalProperties": false
}
```
- <a id='profile-oscal_version'>**OSCAL version**</a>: OSCAL model version.
```json
{
  "title": "OSCAL version",
  "description": "OSCAL model version.",
  "$id": "#/definitions/oscal-version",
  "type": "string"
}
```
- <a id='profile-parameter'>**Parameter**</a>: Parameters provide a mechanism for the dynamic assignment of value(s) in a control.
```json
{
  "title": "Parameter",
  "description": "Parameters provide a mechanism for the dynamic assignment of value(s) in a control.",
  "$id": "#/definitions/param",
  "type": "object",
  "properties": {
    "id": {
      "title": "Identifier",
      "description": "Unique identifier of the containing object",
      "type": "string"
    },
    "class": {
      "title": "Class",
      "description": "Indicating the type or classification of the containing object",
      "type": "string"
    },
    "depends-on": {
      "title": "Depends on",
      "description": "Another parameter invoking this one",
      "type": "string"
    },
    "label": {
      "$ref": "#/definitions/label"
    },
    "descriptions": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/usage"
      }
    },
    "constraints": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/constraint"
      }
    },
    "guidance": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/guideline"
      }
    },
    "value": {
      "$ref": "#/definitions/value"
    },
    "select": {
      "$ref": "#/definitions/select"
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    }
  },
  "required": [
    "id"
  ],
  "additionalProperties": false
}
```
- <a id='profile-part'>**Part**</a>: A partition or component of a control or part
```json
{
  "title": "Part",
  "description": "A partition or component of a control or part",
  "$id": "#/definitions/part",
  "type": "object",
  "properties": {
    "id": {
      "title": "Identifier",
      "description": "Unique identifier of the containing object",
      "type": "string"
    },
    "name": {
      "title": "Name",
      "description": "Identifying the purpose and intended use of the property, part or other object.",
      "type": "string"
    },
    "ns": {
      "title": "Namespace",
      "description": "A namespace qualifying the name.",
      "type": "string"
    },
    "class": {
      "title": "Class",
      "description": "Indicating the type or classification of the containing object",
      "type": "string"
    },
    "title": {
      "$ref": "#/definitions/title"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "prose": {
      "$ref": "#/definitions/prose"
    },
    "parts": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/part"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    }
  },
  "required": [
    "name"
  ],
  "additionalProperties": false
}
```
- <a id='profile-party_(organization_or_person)'>**Party (organization or person)**</a>: A responsible entity, either singular (an organization or person) or collective (multiple persons)
```json
{
  "title": "Party (organization or person)",
  "description": "A responsible entity, either singular (an organization or person) or collective (multiple persons)",
  "$id": "#/definitions/party",
  "type": "object",
  "properties": {
    "uuid": {
      "title": "Universally Unique Identifier",
      "description": "A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "type": {
      "title": "Party Type",
      "description": "A category describing the kind of party the object describes.",
      "type": "string",
      "enum": [
        "person",
        "organization"
      ]
    },
    "party-name": {
      "$ref": "#/definitions/party-name"
    },
    "short-name": {
      "$ref": "#/definitions/short-name"
    },
    "external-ids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/external-id"
      }
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "addresses": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/address"
      }
    },
    "email-addresses": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/email"
      }
    },
    "telephone-numbers": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/phone"
      }
    },
    "member-of-organizations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/member-of-organization"
      }
    },
    "location-uuids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/location-uuid"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "uuid",
    "type",
    "party-name"
  ],
  "additionalProperties": false
}
```
- <a id='profile-party_name'>**Party Name**</a>: The full (legal) name of the party.
```json
{
  "title": "Party Name",
  "description": "The full (legal) name of the party.",
  "$id": "#/definitions/party-name",
  "type": "string"
}
```
- <a id='profile-party_reference'>**Party Reference**</a>: References a party defined in metadata.
```json
{
  "title": "Party Reference",
  "description": "References a party defined in metadata.",
  "$id": "#/definitions/party-uuid",
  "type": "string",
  "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
}
```
- <a id='profile-telephone'>**Telephone**</a>: Contact number by telephone
```json
{
  "title": "Telephone",
  "description": "Contact number by telephone",
  "$id": "#/definitions/phone",
  "type": "object",
  "properties": {
    "type": {
      "description": "Indicates the type of phone number.",
      "type": "string"
    },
    "number": {
      "type": "string"
    }
  },
  "required": [
    "number"
  ],
  "additionalProperties": false
}
```
- <a id='profile-postal_code'>**Postal Code**</a>: Postal or ZIP code for mailing address
```json
{
  "title": "Postal Code",
  "description": "Postal or ZIP code for mailing address",
  "$id": "#/definitions/postal-code",
  "type": "string"
}
```
- <a id='profile-profile'>**Profile**</a>: Each OSCAL profile is defined by a Profile element
```json
{
  "title": "Profile",
  "description": "Each OSCAL profile is defined by a Profile element",
  "$id": "#/definitions/profile",
  "type": "object",
  "properties": {
    "uuid": {
      "title": "Universally Unique Identifier",
      "description": "A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "metadata": {
      "$ref": "#/definitions/metadata"
    },
    "imports": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/import"
      }
    },
    "merge": {
      "$ref": "#/definitions/merge"
    },
    "modify": {
      "$ref": "#/definitions/modify"
    },
    "back-matter": {
      "$ref": "#/definitions/back-matter"
    }
  },
  "required": [
    "uuid",
    "metadata",
    "imports"
  ],
  "additionalProperties": false
}
```
- <a id='profile-property'>**Property**</a>: A value with a name, attributed to the containing control, part, or group.
```json
{
  "title": "Property",
  "description": "A value with a name, attributed to the containing control, part, or group.",
  "$id": "#/definitions/prop",
  "type": "object",
  "properties": {
    "name": {
      "title": "Name",
      "description": "Identifying the purpose and intended use of the property, part or other object.",
      "type": "string"
    },
    "id": {
      "title": "Identifier",
      "description": "Unique identifier of the containing object",
      "type": "string"
    },
    "ns": {
      "title": "Namespace",
      "description": "A namespace qualifying the name.",
      "type": "string"
    },
    "class": {
      "title": "Class",
      "description": "Indicating the type or classification of the containing object",
      "type": "string"
    },
    "value": {
      "type": "string"
    }
  },
  "required": [
    "value",
    "name"
  ],
  "additionalProperties": false
}
```
- <a id='profile-prose'>**Prose**</a>: Prose permits multiple paragraphs, lists, tables etc.
```json
{
  "title": "Prose",
  "description": "Prose permits multiple paragraphs, lists, tables etc.",
  "$id": "#/definitions/prose",
  "type": "string"
}
```
- <a id='profile-publication_timestamp'>**Publication Timestamp**</a>: The date and time this document was published.
```json
{
  "title": "Publication Timestamp",
  "description": "The date and time this document was published.",
  "$id": "#/definitions/published",
  "type": "string",
  "format": "date-time",
  "pattern": "^((2000|2400|2800|(19|2[0-9](0[48]|[2468][048]|[13579][26])))-02-29)|(((19|2[0-9])[0-9]{2})-02-(0[1-9]|1[0-9]|2[0-8]))|(((19|2[0-9])[0-9]{2})-(0[13578]|10|12)-(0[1-9]|[12][0-9]|3[01]))|(((19|2[0-9])[0-9]{2})-(0[469]|11)-(0[1-9]|[12][0-9]|30))T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\\.[0-9]+)?(Z|[+-][0-9]{2}:[0-9]{2})$"
}
```
- <a id='profile-remarks'>**Remarks**</a>: Additional commentary on the parent item.
```json
{
  "title": "Remarks",
  "description": "Additional commentary on the parent item.",
  "$id": "#/definitions/remarks",
  "type": "string"
}
```
- <a id='profile-removal'>**Removal**</a>: Specifies elements to be removed from a control, in resolution
```json
{
  "title": "Removal",
  "description": "Specifies elements to be removed from a control, in resolution",
  "$id": "#/definitions/remove",
  "type": "object",
  "properties": {
    "name-ref": {
      "title": "Reference by (assigned) name",
      "description": "Items to remove, by assigned name",
      "type": "string"
    },
    "class-ref": {
      "title": "Reference by class",
      "description": "Items to remove, by class. A token match.",
      "type": "string"
    },
    "id-ref": {
      "title": "Reference by ID",
      "description": "Items to remove, indicated by their IDs",
      "type": "string"
    },
    "item-name": {
      "title": "References by item name or generic identifier",
      "description": "Items to remove, by the name of the item's type, or generic identifier, e.g. title or prop",
      "type": "string"
    }
  },
  "additionalProperties": false
}
```
- <a id='profile-resource'>**Resource**</a>: A resource associated with the present document, which may be a pointer to other data or a citation.
```json
{
  "title": "Resource",
  "description": "A resource associated with the present document, which may be a pointer to other data or a citation.",
  "$id": "#/definitions/resource",
  "type": "object",
  "properties": {
    "uuid": {
      "title": "Universally Unique Identifier",
      "description": "A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "title": {
      "$ref": "#/definitions/title"
    },
    "desc": {
      "$ref": "#/definitions/desc"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "document-ids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/doc-id"
      }
    },
    "citation": {
      "$ref": "#/definitions/citation"
    },
    "rlinks": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/rlink"
      }
    },
    "attachments": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/base64"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "uuid"
  ],
  "additionalProperties": false
}
```
- <a id='profile-responsible_party'>**Responsible Party**</a>: A reference to a set of organizations or persons that have responsibility for performing a referenced role relative to the parent context.
```json
{
  "title": "Responsible Party",
  "description": "A reference to a set of organizations or persons that have responsibility for performing a referenced role relative to the parent context.",
  "$id": "#/definitions/responsible-party",
  "type": "object",
  "properties": {
    "party-uuids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/party-uuid"
      }
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "party-uuids"
  ],
  "additionalProperties": false
}
```
- <a id='profile-revision_history_entry'>**Revision History Entry**</a>: An entry in a sequential list of revisions to the containing document in reverse chronological order (i.e., most recent previous revision first).
```json
{
  "title": "Revision History Entry",
  "description": "An entry in a sequential list of revisions to the containing document in reverse chronological order (i.e., most recent previous revision first).",
  "$id": "#/definitions/revision",
  "type": "object",
  "properties": {
    "title": {
      "$ref": "#/definitions/title"
    },
    "published": {
      "$ref": "#/definitions/published"
    },
    "last-modified": {
      "$ref": "#/definitions/last-modified"
    },
    "version": {
      "$ref": "#/definitions/version"
    },
    "oscal-version": {
      "$ref": "#/definitions/oscal-version"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "additionalProperties": false
}
```
- <a id='profile-resource_link'>**Resource link**</a>: A pointer to an external copy of a document with optional hash for verification
```json
{
  "title": "Resource link",
  "description": "A pointer to an external copy of a document with optional hash for verification",
  "$id": "#/definitions/rlink",
  "type": "object",
  "properties": {
    "href": {
      "title": "hypertext reference",
      "description": "A link to a document or document fragment (actual, nominal or projected)",
      "type": "string",
      "format": "uri-reference"
    },
    "media-type": {
      "title": "Media type",
      "description": "Describes the media type of the linked resource",
      "type": "string"
    },
    "hashes": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/hash"
      }
    }
  },
  "required": [
    "href"
  ],
  "additionalProperties": false
}
```
- <a id='profile-role'>**Role**</a>: Defining a role to be assigned to a party
```json
{
  "title": "Role",
  "description": "Defining a role to be assigned to a party",
  "$id": "#/definitions/role",
  "type": "object",
  "properties": {
    "id": {
      "title": "Identifier",
      "description": "Unique identifier of the containing object",
      "type": "string"
    },
    "title": {
      "$ref": "#/definitions/title"
    },
    "short-name": {
      "$ref": "#/definitions/short-name"
    },
    "desc": {
      "$ref": "#/definitions/desc"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "id",
    "title"
  ],
  "additionalProperties": false
}
```
- <a id='profile-selection'>**Selection**</a>: Presenting a choice among alternatives
```json
{
  "title": "Selection",
  "description": "Presenting a choice among alternatives",
  "$id": "#/definitions/select",
  "type": "object",
  "properties": {
    "how-many": {
      "title": "Cardinality",
      "description": "When selecting, a requirement such as one or more",
      "type": "string"
    },
    "alternatives": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/choice"
      }
    }
  },
  "additionalProperties": false
}
```
- <a id='profile-parameter_setting'>**Parameter Setting**</a>: A parameter setting, to be propagated to points of insertion
```json
{
  "title": "Parameter Setting",
  "description": "A parameter setting, to be propagated to points of insertion",
  "$id": "#/definitions/set-parameter",
  "type": "object",
  "properties": {
    "class": {
      "title": "Class",
      "description": "Indicating the type or classification of the containing object",
      "type": "string"
    },
    "depends-on": {
      "title": "Depends on",
      "description": "Another parameter invoking this one",
      "type": "string"
    },
    "label": {
      "$ref": "#/definitions/label"
    },
    "descriptions": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/usage"
      }
    },
    "constraints": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/constraint"
      }
    },
    "guidance": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/guideline"
      }
    },
    "value": {
      "$ref": "#/definitions/value"
    },
    "select": {
      "$ref": "#/definitions/select"
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    }
  },
  "additionalProperties": false
}
```
- <a id='profile-short-name'>**short-name**</a>: A common name, short name or acronym
```json
{
  "title": "short-name",
  "description": "A common name, short name or acronym",
  "$id": "#/definitions/short-name",
  "type": "string"
}
```
- <a id='profile-state'>**State**</a>: State, province or analogous geographical region for mailing address
```json
{
  "title": "State",
  "description": "State, province or analogous geographical region for mailing address",
  "$id": "#/definitions/state",
  "type": "string"
}
```
- <a id='profile-text'>**Text**</a>: A line of textual content whose semantic is determined by the context of use.
```json
{
  "title": "Text",
  "description": "A line of textual content whose semantic is determined by the context of use.",
  "$id": "#/definitions/text",
  "type": "string"
}
```
- <a id='profile-title'>**Title**</a>: A title for display and navigation
```json
{
  "title": "Title",
  "description": "A title for display and navigation",
  "$id": "#/definitions/title",
  "type": "string"
}
```
- <a id='profile-url'>**URL**</a>: URL for web site or Internet presence
```json
{
  "title": "URL",
  "description": "URL for web site or Internet presence",
  "$id": "#/definitions/url",
  "type": "string",
  "format": "uri"
}
```
- <a id='profile-parameter_description'>**Parameter description**</a>: Indicates and explains the purpose and use of a parameter
```json
{
  "title": "Parameter description",
  "description": "Indicates and explains the purpose and use of a parameter",
  "$id": "#/definitions/usage",
  "type": "object",
  "properties": {
    "id": {
      "title": "Identifier",
      "description": "Unique identifier of the containing object",
      "type": "string"
    },
    "summary": {
      "type": "string"
    }
  },
  "required": [
    "summary"
  ],
  "additionalProperties": false
}
```
- <a id='profile-value_constraint'>**Value constraint**</a>: Indicates a permissible value for a parameter or property
```json
{
  "title": "Value constraint",
  "description": "Indicates a permissible value for a parameter or property",
  "$id": "#/definitions/value",
  "type": "string"
}
```
- <a id='profile-document_version'>**Document version**</a>: The version of the document content.
```json
{
  "title": "Document version",
  "description": "The version of the document content.",
  "$id": "#/definitions/version",
  "type": "string"
}
```

## ssp

> OSCAL System Security Plan (SSP) Format

- <a id='ssp-address_line'>**Address line**</a>: A single line of an address.
```json
{
  "title": "Address line",
  "description": "A single line of an address.",
  "$id": "#/definitions/addr-line",
  "type": "string"
}
```
- <a id='ssp-address'>**Address**</a>: A postal address.
```json
{
  "title": "Address",
  "description": "A postal address.",
  "$id": "#/definitions/address",
  "type": "object",
  "properties": {
    "type": {
      "description": "Indicates the type of address.",
      "type": "string"
    },
    "postal-address": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/addr-line"
      }
    },
    "city": {
      "$ref": "#/definitions/city"
    },
    "state": {
      "$ref": "#/definitions/state"
    },
    "postal-code": {
      "$ref": "#/definitions/postal-code"
    },
    "country": {
      "$ref": "#/definitions/country"
    }
  },
  "additionalProperties": false
}
```
- <a id='ssp-adjustment_justification'>**Adjustment Justification**</a>: If the selected security level is different from the base security level, this contains the justification for the change.
```json
{
  "title": "Adjustment Justification",
  "description": "If the selected security level is different from the base security level, this contains the justification for the change.",
  "$id": "#/definitions/adjustment-justification",
  "type": "string"
}
```
- <a id='ssp-annotation'>**Annotation**</a>: A name/value pair with optional explanatory remarks.
```json
{
  "title": "Annotation",
  "description": "A name/value pair with optional explanatory remarks.",
  "$id": "#/definitions/annotation",
  "type": "object",
  "properties": {
    "name": {
      "title": "Name",
      "description": "Identifying the purpose and intended use of the property, part or other object.",
      "type": "string"
    },
    "id": {
      "title": "Identifier",
      "description": "Unique identifier of the containing object",
      "type": "string"
    },
    "ns": {
      "title": "Namespace",
      "description": "A namespace qualifying the name.",
      "type": "string"
    },
    "value": {
      "title": "Value",
      "description": "Indicates the value of the characteristic.",
      "type": "string"
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "name"
  ],
  "additionalProperties": false
}
```
- <a id='ssp-authorization_boundary'>**Authorization Boundary**</a>: A description of this system's authorization boundary, optionally supplemented by diagrams that illustrate the authorization boundary.
```json
{
  "title": "Authorization Boundary",
  "description": "A description of this system's authorization boundary, optionally supplemented by diagrams that illustrate the authorization boundary.",
  "$id": "#/definitions/authorization-boundary",
  "type": "object",
  "properties": {
    "description": {
      "$ref": "#/definitions/description"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "diagrams": {
      "type": "object",
      "minProperties": 1,
      "additionalProperties": {
        "allOf": [
          {
            "type": "object",
            "$ref": "#/definitions/diagram"
          },
          {
            "not": {
              "type": "string"
            }
          }
        ]
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "description"
  ],
  "additionalProperties": false
}
```
- <a id='ssp-privilege'>**Privilege**</a>: Identifies a specific system privilege held by the user, along with an associated description and/or rationale for the privilege.
```json
{
  "title": "Privilege",
  "description": "Identifies a specific system privilege held by the user, along with an associated description and/or rationale for the privilege.",
  "$id": "#/definitions/authorized-privilege",
  "type": "object",
  "properties": {
    "title": {
      "$ref": "#/definitions/title"
    },
    "description": {
      "$ref": "#/definitions/description"
    },
    "functions-performed": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/function-performed"
      }
    }
  },
  "required": [
    "title",
    "functions-performed"
  ],
  "additionalProperties": false
}
```
- <a id='ssp-availability_impact_level'>**Availability Impact Level**</a>: The expected level of impact resulting from the disruption of access to or use of information or the information system.
```json
{
  "title": "Availability Impact Level",
  "description": "The expected level of impact resulting from the disruption of access to or use of information or the information system.",
  "$id": "#/definitions/availability-impact",
  "type": "object",
  "properties": {
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "base": {
      "$ref": "#/definitions/base"
    },
    "selected": {
      "$ref": "#/definitions/selected"
    },
    "adjustment-justification": {
      "$ref": "#/definitions/adjustment-justification"
    }
  },
  "required": [
    "base"
  ],
  "additionalProperties": false
}
```
- <a id='ssp-back_matter'>**Back matter**</a>: A collection of citations and resource references.
```json
{
  "title": "Back matter",
  "description": "A collection of citations and resource references.",
  "$id": "#/definitions/back-matter",
  "type": "object",
  "properties": {
    "resources": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/resource"
      }
    }
  },
  "additionalProperties": false
}
```
- <a id='ssp-base_level_(confidentiality,_integrity,_or_availability)'>**Base Level (Confidentiality, Integrity, or Availability)**</a>: The prescribed base (Confidentiality, Integrity, or Availability) security impact level.
```json
{
  "title": "Base Level (Confidentiality, Integrity, or Availability)",
  "description": "The prescribed base (Confidentiality, Integrity, or Availability) security impact level.",
  "$id": "#/definitions/base",
  "type": "string",
  "enum": [
    "fips-199-low",
    "fips-199-moderate",
    "fips-199-high"
  ]
}
```
- <a id='ssp-base64'>**Base64**</a>: 
```json
{
  "title": "Base64",
  "description": "",
  "$id": "#/definitions/base64",
  "type": "object",
  "properties": {
    "filename": {
      "title": "File Name",
      "description": "Name of the file before it was encoded as Base64 to be embedded in a resource. This is the name that will be assigned to the file when the file is decoded.",
      "type": "string",
      "format": "uri-reference"
    },
    "media-type": {
      "title": "Media type",
      "description": "Describes the media type of the linked resource",
      "type": "string"
    },
    "value": {
      "type": "string"
    }
  },
  "required": [
    "value"
  ],
  "additionalProperties": false
}
```
- <a id='ssp-bibliographic_definition'>**Bibliographic Definition**</a>: A container in which a set of bibliographic information can included. The model of this information is undefined by OSCAL.
```json
{
  "title": "Bibliographic Definition",
  "description": "A container in which a set of bibliographic information can included. The model of this information is undefined by OSCAL.",
  "$id": "#/definitions/biblio",
  "type": "object",
  "additionalProperties": false
}
```
- <a id='ssp-component_control_implementation'>**Component Control Implementation**</a>: Defines how the referenced component implements a set of controls.
```json
{
  "title": "Component Control Implementation",
  "description": "Defines how the referenced component implements a set of controls.",
  "$id": "#/definitions/by-component",
  "type": "object",
  "properties": {
    "uuid": {
      "title": "Universally Unique Identifier",
      "description": "A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "description": {
      "$ref": "#/definitions/description"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "responsible-roles": {
      "type": "object",
      "minProperties": 1,
      "additionalProperties": {
        "allOf": [
          {
            "type": "object",
            "$ref": "#/definitions/responsible-role"
          },
          {
            "not": {
              "type": "string"
            }
          }
        ]
      }
    },
    "parameter-settings": {
      "type": "object",
      "minProperties": 1,
      "additionalProperties": {
        "allOf": [
          {
            "type": "object",
            "$ref": "#/definitions/set-parameter"
          },
          {
            "not": {
              "type": "string"
            }
          }
        ]
      }
    }
  },
  "required": [
    "uuid",
    "description"
  ],
  "additionalProperties": false
}
```
- <a id='ssp-caption'>**Caption**</a>: A brief caption to annotate the diagram.
```json
{
  "title": "Caption",
  "description": "A brief caption to annotate the diagram.",
  "$id": "#/definitions/caption",
  "type": "string"
}
```
- <a id='ssp-citation'>**Citation**</a>: A citation consisting of end note text and optional structured bibliographic data.
```json
{
  "title": "Citation",
  "description": "A citation consisting of end note text and optional structured bibliographic data.",
  "$id": "#/definitions/citation",
  "type": "object",
  "properties": {
    "text": {
      "$ref": "#/definitions/text"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "biblio": {
      "$ref": "#/definitions/biblio"
    }
  },
  "required": [
    "text"
  ],
  "additionalProperties": false
}
```
- <a id='ssp-city'>**City**</a>: City, town or geographical region for mailing address
```json
{
  "title": "City",
  "description": "City, town or geographical region for mailing address",
  "$id": "#/definitions/city",
  "type": "string"
}
```
- <a id='ssp-component'>**Component**</a>: A defined component that can be part of an implemented system.
```json
{
  "title": "Component",
  "description": "A defined component that can be part of an implemented system.",
  "$id": "#/definitions/component",
  "type": "object",
  "properties": {
    "component-type": {
      "title": "Component Type",
      "description": "A category describing the purpose of the component.",
      "type": "string"
    },
    "title": {
      "$ref": "#/definitions/title"
    },
    "description": {
      "$ref": "#/definitions/description"
    },
    "purpose": {
      "$ref": "#/definitions/purpose"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "status": {
      "$ref": "#/definitions/status"
    },
    "responsible-roles": {
      "type": "object",
      "minProperties": 1,
      "additionalProperties": {
        "allOf": [
          {
            "type": "object",
            "$ref": "#/definitions/responsible-role"
          },
          {
            "not": {
              "type": "string"
            }
          }
        ]
      }
    },
    "protocols": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/protocol"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "component-type",
    "title",
    "description",
    "status"
  ],
  "additionalProperties": false
}
```
- <a id='ssp-confidentiality_impact_level'>**Confidentiality Impact Level**</a>: The expected level of impact resulting from the unauthorized disclosure of information.
```json
{
  "title": "Confidentiality Impact Level",
  "description": "The expected level of impact resulting from the unauthorized disclosure of information.",
  "$id": "#/definitions/confidentiality-impact",
  "type": "object",
  "properties": {
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "base": {
      "$ref": "#/definitions/base"
    },
    "selected": {
      "$ref": "#/definitions/selected"
    },
    "adjustment-justification": {
      "$ref": "#/definitions/adjustment-justification"
    }
  },
  "required": [
    "base"
  ],
  "additionalProperties": false
}
```
- <a id='ssp-control_implementation'>**Control Implementation**</a>: Describes how the system satisfies a set of controls.
```json
{
  "title": "Control Implementation",
  "description": "Describes how the system satisfies a set of controls.",
  "$id": "#/definitions/control-implementation",
  "type": "object",
  "properties": {
    "description": {
      "$ref": "#/definitions/description"
    },
    "implemented-requirements": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/implemented-requirement"
      }
    }
  },
  "required": [
    "description",
    "implemented-requirements"
  ],
  "additionalProperties": false
}
```
- <a id='ssp-country'>**Country**</a>: Country for mailing address
```json
{
  "title": "Country",
  "description": "Country for mailing address",
  "$id": "#/definitions/country",
  "type": "string"
}
```
- <a id='ssp-data_flow'>**Data Flow**</a>: A description of the logical flow of information within the system and across its boundaries, optionally supplemented by diagrams that illustrate these flows.
```json
{
  "title": "Data Flow",
  "description": "A description of the logical flow of information within the system and across its boundaries, optionally supplemented by diagrams that illustrate these flows.",
  "$id": "#/definitions/data-flow",
  "type": "object",
  "properties": {
    "description": {
      "$ref": "#/definitions/description"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "diagrams": {
      "type": "object",
      "minProperties": 1,
      "additionalProperties": {
        "allOf": [
          {
            "type": "object",
            "$ref": "#/definitions/diagram"
          },
          {
            "not": {
              "type": "string"
            }
          }
        ]
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "description"
  ],
  "additionalProperties": false
}
```
- <a id='ssp-system_authorization_date'>**System Authorization Date**</a>: The date this system received its authorization.
```json
{
  "title": "System Authorization Date",
  "description": "The date this system received its authorization.",
  "$id": "#/definitions/date-authorized",
  "type": "string",
  "pattern": "^((2000|2400|2800|(19|2[0-9](0[48]|[2468][048]|[13579][26])))-02-29)|(((19|2[0-9])[0-9]{2})-02-(0[1-9]|1[0-9]|2[0-8]))|(((19|2[0-9])[0-9]{2})-(0[13578]|10|12)-(0[1-9]|[12][0-9]|3[01]))|(((19|2[0-9])[0-9]{2})-(0[469]|11)-(0[1-9]|[12][0-9]|30))(Z|[+-][0-9]{2}:[0-9]{2})?$"
}
```
- <a id='ssp-description'>**Description**</a>: A short textual description
```json
{
  "title": "Description",
  "description": "A short textual description",
  "$id": "#/definitions/desc",
  "type": "string"
}
```
- <a id='ssp-description'>**Description**</a>: A description supporting the parent item.
```json
{
  "title": "Description",
  "description": "A description supporting the parent item.",
  "$id": "#/definitions/description",
  "type": "string"
}
```
- <a id='ssp-diagram'>**Diagram**</a>: A graphic that provides a visual representation the system, or some aspect of it.
```json
{
  "title": "Diagram",
  "description": "A graphic that provides a visual representation the system, or some aspect of it.",
  "$id": "#/definitions/diagram",
  "type": "object",
  "properties": {
    "description": {
      "$ref": "#/definitions/description"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "caption": {
      "$ref": "#/definitions/caption"
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "additionalProperties": false
}
```
- <a id='ssp-document_identifier'>**Document Identifier**</a>: A document identifier qualified by an identifier type.
```json
{
  "title": "Document Identifier",
  "description": "A document identifier qualified by an identifier type.",
  "$id": "#/definitions/doc-id",
  "type": "object",
  "properties": {
    "type": {
      "description": "Qualifies the kind of document identifier.",
      "type": "string"
    },
    "identifier": {
      "type": "string"
    }
  },
  "required": [
    "identifier",
    "type"
  ],
  "additionalProperties": false
}
```
- <a id='ssp-email'>**Email**</a>: Email address
```json
{
  "title": "Email",
  "description": "Email address",
  "$id": "#/definitions/email",
  "type": "string",
  "format": "email",
  "pattern": "^.+@.+"
}
```
- <a id='ssp-personal_identifier'>**Personal Identifier**</a>: An identifier for a person (such as an ORCID) using a designated scheme.
```json
{
  "title": "Personal Identifier",
  "description": "An identifier for a person (such as an ORCID) using a designated scheme.",
  "$id": "#/definitions/external-id",
  "type": "object",
  "properties": {
    "type": {
      "title": "Type",
      "description": "Indicating the type of identifier, address, email or other data item.",
      "type": "string"
    },
    "id": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "type"
  ],
  "additionalProperties": false
}
```
- <a id='ssp-functions_performed'>**Functions Performed**</a>: Describes a function performed for a given authorized privilege by this user class.
```json
{
  "title": "Functions Performed",
  "description": "Describes a function performed for a given authorized privilege by this user class.",
  "$id": "#/definitions/function-performed",
  "type": "string"
}
```
- <a id='ssp-hash'>**Hash**</a>: A representation of a cryptographic digest generated over a resource using a hash algorithm.
```json
{
  "title": "Hash",
  "description": "A representation of a cryptographic digest generated over a resource using a hash algorithm.",
  "$id": "#/definitions/hash",
  "type": "object",
  "properties": {
    "algorithm": {
      "title": "Hash algorithm",
      "description": "Method by which a hash is derived",
      "type": "string"
    },
    "value": {
      "type": "string"
    }
  },
  "required": [
    "value",
    "algorithm"
  ],
  "additionalProperties": false
}
```
- <a id='ssp-implemented_component'>**Implemented Component**</a>: The set of componenets that are implemented in a given system inventory item.
```json
{
  "title": "Implemented Component",
  "description": "The set of componenets that are implemented in a given system inventory item.",
  "$id": "#/definitions/implemented-component",
  "type": "object",
  "properties": {
    "use": {
      "title": "Implementation Use Type",
      "description": "The type of implementation",
      "type": "string"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "responsible-parties": {
      "type": "object",
      "minProperties": 1,
      "additionalProperties": {
        "allOf": [
          {
            "type": "object",
            "$ref": "#/definitions/responsible-party"
          },
          {
            "not": {
              "type": "string"
            }
          }
        ]
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "additionalProperties": false
}
```
- <a id='ssp-control-based_requirement'>**Control-based Requirement**</a>: Describes how the system satisfies an individual control.
```json
{
  "title": "Control-based Requirement",
  "description": "Describes how the system satisfies an individual control.",
  "$id": "#/definitions/implemented-requirement",
  "type": "object",
  "properties": {
    "uuid": {
      "title": "Universally Unique Identifier",
      "description": "A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "control-id": {
      "title": "Control Identifier Reference",
      "description": "A reference to a control identifier.",
      "type": "string"
    },
    "description": {
      "$ref": "#/definitions/description"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "by-components": {
      "type": "object",
      "minProperties": 1,
      "additionalProperties": {
        "allOf": [
          {
            "type": "object",
            "$ref": "#/definitions/by-component"
          },
          {
            "not": {
              "type": "string"
            }
          }
        ]
      }
    },
    "responsible-roles": {
      "type": "object",
      "minProperties": 1,
      "additionalProperties": {
        "allOf": [
          {
            "type": "object",
            "$ref": "#/definitions/responsible-role"
          },
          {
            "not": {
              "type": "string"
            }
          }
        ]
      }
    },
    "parameter-settings": {
      "type": "object",
      "minProperties": 1,
      "additionalProperties": {
        "allOf": [
          {
            "type": "object",
            "$ref": "#/definitions/set-parameter"
          },
          {
            "not": {
              "type": "string"
            }
          }
        ]
      }
    },
    "statements": {
      "type": "object",
      "minProperties": 1,
      "additionalProperties": {
        "allOf": [
          {
            "type": "object",
            "$ref": "#/definitions/statement"
          },
          {
            "not": {
              "type": "string"
            }
          }
        ]
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "uuid",
    "control-id"
  ],
  "additionalProperties": false
}
```
- <a id='ssp-import_profile'>**Import Profile**</a>: Used to import the OSCAL profile representing the system's control baseline.
```json
{
  "title": "Import Profile",
  "description": "Used to import the OSCAL profile representing the system's control baseline.",
  "$id": "#/definitions/import-profile",
  "type": "object",
  "properties": {
    "href": {
      "title": "hypertext reference",
      "description": "A link to a document or document fragment (actual, nominal or projected)",
      "type": "string",
      "format": "uri-reference"
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "href"
  ],
  "additionalProperties": false
}
```
- <a id='ssp-information_type'>**Information Type**</a>: Contains details about one information type that is stored, processed, or transmitted by the system, such as privacy information, and those defined in NIST SP 800-60.
```json
{
  "title": "Information Type",
  "description": "Contains details about one information type that is stored, processed, or transmitted by the system, such as privacy information, and those defined in NIST SP 800-60.",
  "$id": "#/definitions/information-type",
  "type": "object",
  "properties": {
    "id": {
      "title": "Identifier",
      "description": "Unique identifier of the containing object",
      "type": "string"
    },
    "title": {
      "$ref": "#/definitions/title"
    },
    "description": {
      "$ref": "#/definitions/description"
    },
    "information-type-ids": {
      "type": "object",
      "minProperties": 1,
      "additionalProperties": {
        "allOf": [
          {
            "type": "object",
            "$ref": "#/definitions/information-type-id"
          },
          {
            "not": {
              "type": "string"
            }
          }
        ]
      }
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "confidentiality-impact": {
      "$ref": "#/definitions/confidentiality-impact"
    },
    "integrity-impact": {
      "$ref": "#/definitions/integrity-impact"
    },
    "availability-impact": {
      "$ref": "#/definitions/availability-impact"
    }
  },
  "required": [
    "title",
    "description",
    "confidentiality-impact",
    "integrity-impact",
    "availability-impact"
  ],
  "additionalProperties": false
}
```
- <a id='ssp-information_type_identifier'>**Information Type Identifier**</a>: An identifier qualified by the given identification system used, such as NIST SP 800-60.
```json
{
  "title": "Information Type Identifier",
  "description": "An identifier qualified by the given identification system used, such as NIST SP 800-60.",
  "$id": "#/definitions/information-type-id",
  "type": "object",
  "properties": {
    "id": {
      "type": "string"
    }
  },
  "required": [
    "id"
  ],
  "additionalProperties": false
}
```
- <a id='ssp-integrity_impact_level'>**Integrity Impact Level**</a>: The expected level of impact resulting from the unauthorized modification of information.
```json
{
  "title": "Integrity Impact Level",
  "description": "The expected level of impact resulting from the unauthorized modification of information.",
  "$id": "#/definitions/integrity-impact",
  "type": "object",
  "properties": {
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "base": {
      "$ref": "#/definitions/base"
    },
    "selected": {
      "$ref": "#/definitions/selected"
    },
    "adjustment-justification": {
      "$ref": "#/definitions/adjustment-justification"
    }
  },
  "required": [
    "base"
  ],
  "additionalProperties": false
}
```
- <a id='ssp-inventory_item'>**Inventory Item**</a>: A single managed inventory item within the system.
```json
{
  "title": "Inventory Item",
  "description": "A single managed inventory item within the system.",
  "$id": "#/definitions/inventory-item",
  "type": "object",
  "properties": {
    "asset-id": {
      "title": "Asset Identifier",
      "description": "Organizational asset identifier that is unique in the context of the system. This may be a reference to the identifier used in an asset tracking system or a vulnerability scanning tool.",
      "type": "string"
    },
    "description": {
      "$ref": "#/definitions/description"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "responsible-parties": {
      "type": "object",
      "minProperties": 1,
      "additionalProperties": {
        "allOf": [
          {
            "type": "object",
            "$ref": "#/definitions/responsible-party"
          },
          {
            "not": {
              "type": "string"
            }
          }
        ]
      }
    },
    "implemented-components": {
      "type": "object",
      "minProperties": 1,
      "additionalProperties": {
        "allOf": [
          {
            "type": "object",
            "$ref": "#/definitions/implemented-component"
          },
          {
            "not": {
              "type": "string"
            }
          }
        ]
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "asset-id",
    "description"
  ],
  "additionalProperties": false
}
```
- <a id='ssp-last_modified_timestamp'>**Last modified timestamp**</a>: Date and time of last modification.
```json
{
  "title": "Last modified timestamp",
  "description": "Date and time of last modification.",
  "$id": "#/definitions/last-modified",
  "type": "string",
  "format": "date-time",
  "pattern": "^((2000|2400|2800|(19|2[0-9](0[48]|[2468][048]|[13579][26])))-02-29)|(((19|2[0-9])[0-9]{2})-02-(0[1-9]|1[0-9]|2[0-8]))|(((19|2[0-9])[0-9]{2})-(0[13578]|10|12)-(0[1-9]|[12][0-9]|3[01]))|(((19|2[0-9])[0-9]{2})-(0[469]|11)-(0[1-9]|[12][0-9]|30))T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\\.[0-9]+)?(Z|[+-][0-9]{2}:[0-9]{2})$"
}
```
- <a id='ssp-leveraged_authorization'>**Leveraged Authorization**</a>: A description of another authorized system from which this system inherits capabilities that satisfy security requirements. Another term for this concept is a common control provider.
```json
{
  "title": "Leveraged Authorization",
  "description": "A description of another authorized system from which this system inherits capabilities that satisfy security requirements. Another term for this concept is a common control provider.",
  "$id": "#/definitions/leveraged-authorization",
  "type": "object",
  "properties": {
    "id": {
      "title": "Identifier",
      "description": "Unique identifier of the containing object",
      "type": "string"
    },
    "title": {
      "$ref": "#/definitions/title"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "party-uuid": {
      "$ref": "#/definitions/party-uuid"
    },
    "date-authorized": {
      "$ref": "#/definitions/date-authorized"
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "title",
    "party-uuid",
    "date-authorized"
  ],
  "additionalProperties": false
}
```
- <a id='ssp-link'>**Link**</a>: A reference to a local or remote resource
```json
{
  "title": "Link",
  "description": "A reference to a local or remote resource",
  "$id": "#/definitions/link",
  "type": "object",
  "properties": {
    "href": {
      "title": "hypertext reference",
      "description": "A link to a document or document fragment (actual, nominal or projected)",
      "type": "string",
      "format": "uri-reference"
    },
    "rel": {
      "title": "Relation",
      "description": "Describes the type of relationship provided by the link. This can be an indicator of the link's purpose.",
      "type": "string"
    },
    "media-type": {
      "title": "Media type",
      "description": "Describes the media type of the linked resource",
      "type": "string"
    },
    "text": {
      "type": "string"
    }
  },
  "required": [
    "text",
    "href"
  ],
  "additionalProperties": false
}
```
- <a id='ssp-location'>**Location**</a>: A location, with associated metadata that can be referenced.
```json
{
  "title": "Location",
  "description": "A location, with associated metadata that can be referenced.",
  "$id": "#/definitions/location",
  "type": "object",
  "properties": {
    "uuid": {
      "title": "Universally Unique Identifier",
      "description": "A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "title": {
      "$ref": "#/definitions/title"
    },
    "address": {
      "$ref": "#/definitions/address"
    },
    "email-addresses": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/email"
      }
    },
    "telephone-numbers": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/phone"
      }
    },
    "URLs": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/url"
      }
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "uuid",
    "address"
  ],
  "additionalProperties": false
}
```
- <a id='ssp-location_reference'>**Location Reference**</a>: References a location defined in metadata.
```json
{
  "title": "Location Reference",
  "description": "References a location defined in metadata.",
  "$id": "#/definitions/location-uuid",
  "type": "string",
  "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
}
```
- <a id='ssp-organizational_affiliation'>**Organizational Affiliation**</a>: Identifies that the containing object is a member of the organization associated with the provided UUID.
```json
{
  "title": "Organizational Affiliation",
  "description": "Identifies that the containing object is a member of the organization associated with the provided UUID.",
  "$id": "#/definitions/member-of-organization",
  "type": "string",
  "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
}
```
- <a id='ssp-publication_metadata'>**Publication metadata**</a>: Provides information about the publication and availability of the containing document.
```json
{
  "title": "Publication metadata",
  "description": "Provides information about the publication and availability of the containing document.",
  "$id": "#/definitions/metadata",
  "type": "object",
  "properties": {
    "title": {
      "$ref": "#/definitions/title"
    },
    "published": {
      "$ref": "#/definitions/published"
    },
    "last-modified": {
      "$ref": "#/definitions/last-modified"
    },
    "version": {
      "$ref": "#/definitions/version"
    },
    "oscal-version": {
      "$ref": "#/definitions/oscal-version"
    },
    "revision-history": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/revision"
      }
    },
    "document-ids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/doc-id"
      }
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "roles": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/role"
      }
    },
    "locations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/location"
      }
    },
    "parties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/party"
      }
    },
    "responsible-parties": {
      "type": "object",
      "minProperties": 1,
      "additionalProperties": {
        "allOf": [
          {
            "type": "object",
            "$ref": "#/definitions/responsible-party"
          },
          {
            "not": {
              "type": "string"
            }
          }
        ]
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "title",
    "last-modified",
    "version",
    "oscal-version"
  ],
  "additionalProperties": false
}
```
- <a id='ssp-network_architecture'>**Network Architecture**</a>: A description of the system's network architecture, optionally supplemented by diagrams that illustrate the network architecture.
```json
{
  "title": "Network Architecture",
  "description": "A description of the system's network architecture, optionally supplemented by diagrams that illustrate the network architecture.",
  "$id": "#/definitions/network-architecture",
  "type": "object",
  "properties": {
    "description": {
      "$ref": "#/definitions/description"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "diagrams": {
      "type": "object",
      "minProperties": 1,
      "additionalProperties": {
        "allOf": [
          {
            "type": "object",
            "$ref": "#/definitions/diagram"
          },
          {
            "not": {
              "type": "string"
            }
          }
        ]
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "description"
  ],
  "additionalProperties": false
}
```
- <a id='ssp-oscal_version'>**OSCAL version**</a>: OSCAL model version.
```json
{
  "title": "OSCAL version",
  "description": "OSCAL model version.",
  "$id": "#/definitions/oscal-version",
  "type": "string"
}
```
- <a id='ssp-party_(organization_or_person)'>**Party (organization or person)**</a>: A responsible entity, either singular (an organization or person) or collective (multiple persons)
```json
{
  "title": "Party (organization or person)",
  "description": "A responsible entity, either singular (an organization or person) or collective (multiple persons)",
  "$id": "#/definitions/party",
  "type": "object",
  "properties": {
    "uuid": {
      "title": "Universally Unique Identifier",
      "description": "A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "type": {
      "title": "Party Type",
      "description": "A category describing the kind of party the object describes.",
      "type": "string",
      "enum": [
        "person",
        "organization"
      ]
    },
    "party-name": {
      "$ref": "#/definitions/party-name"
    },
    "short-name": {
      "$ref": "#/definitions/short-name"
    },
    "external-ids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/external-id"
      }
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "addresses": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/address"
      }
    },
    "email-addresses": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/email"
      }
    },
    "telephone-numbers": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/phone"
      }
    },
    "member-of-organizations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/member-of-organization"
      }
    },
    "location-uuids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/location-uuid"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "uuid",
    "type",
    "party-name"
  ],
  "additionalProperties": false
}
```
- <a id='ssp-party_name'>**Party Name**</a>: The full (legal) name of the party.
```json
{
  "title": "Party Name",
  "description": "The full (legal) name of the party.",
  "$id": "#/definitions/party-name",
  "type": "string"
}
```
- <a id='ssp-party_reference'>**Party Reference**</a>: References a party defined in metadata.
```json
{
  "title": "Party Reference",
  "description": "References a party defined in metadata.",
  "$id": "#/definitions/party-uuid",
  "type": "string",
  "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
}
```
- <a id='ssp-telephone'>**Telephone**</a>: Contact number by telephone
```json
{
  "title": "Telephone",
  "description": "Contact number by telephone",
  "$id": "#/definitions/phone",
  "type": "object",
  "properties": {
    "type": {
      "description": "Indicates the type of phone number.",
      "type": "string"
    },
    "number": {
      "type": "string"
    }
  },
  "required": [
    "number"
  ],
  "additionalProperties": false
}
```
- <a id='ssp-port_range'>**Port Range**</a>: Where applicable this is the IPv4 port range on which the service operates.
```json
{
  "title": "Port Range",
  "description": "Where applicable this is the IPv4 port range on which the service operates.",
  "$id": "#/definitions/port-range",
  "type": "object",
  "properties": {
    "start": {
      "title": "Start",
      "description": "Indicates the starting port number in a port range",
      "type": "integer",
      "multipleOf": 1,
      "minimum": 0
    },
    "end": {
      "title": "End",
      "description": "Indicates the ending port number in a port range",
      "type": "integer",
      "multipleOf": 1,
      "minimum": 0
    },
    "transport": {
      "title": "Transport",
      "description": "Indicates the transport type.",
      "type": "string",
      "enum": [
        "TCP",
        "UDP"
      ]
    }
  },
  "additionalProperties": false
}
```
- <a id='ssp-postal_code'>**Postal Code**</a>: Postal or ZIP code for mailing address
```json
{
  "title": "Postal Code",
  "description": "Postal or ZIP code for mailing address",
  "$id": "#/definitions/postal-code",
  "type": "string"
}
```
- <a id='ssp-property'>**Property**</a>: A value with a name, attributed to the containing control, part, or group.
```json
{
  "title": "Property",
  "description": "A value with a name, attributed to the containing control, part, or group.",
  "$id": "#/definitions/prop",
  "type": "object",
  "properties": {
    "name": {
      "title": "Name",
      "description": "Identifying the purpose and intended use of the property, part or other object.",
      "type": "string"
    },
    "id": {
      "title": "Identifier",
      "description": "Unique identifier of the containing object",
      "type": "string"
    },
    "ns": {
      "title": "Namespace",
      "description": "A namespace qualifying the name.",
      "type": "string"
    },
    "class": {
      "title": "Class",
      "description": "Indicating the type or classification of the containing object",
      "type": "string"
    },
    "value": {
      "type": "string"
    }
  },
  "required": [
    "value",
    "name"
  ],
  "additionalProperties": false
}
```
- <a id='ssp-protocol'>**Protocol**</a>: Information about the protocol used to provide a service.
```json
{
  "title": "Protocol",
  "description": "Information about the protocol used to provide a service.",
  "$id": "#/definitions/protocol",
  "type": "object",
  "properties": {
    "uuid": {
      "title": "Universally Unique Identifier",
      "description": "A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "name": {
      "description": "The short name of the protocol (e.g., TLS).",
      "type": "string"
    },
    "title": {
      "$ref": "#/definitions/title"
    },
    "port-ranges": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/port-range"
      }
    }
  },
  "required": [
    "name"
  ],
  "additionalProperties": false
}
```
- <a id='ssp-publication_timestamp'>**Publication Timestamp**</a>: The date and time this document was published.
```json
{
  "title": "Publication Timestamp",
  "description": "The date and time this document was published.",
  "$id": "#/definitions/published",
  "type": "string",
  "format": "date-time",
  "pattern": "^((2000|2400|2800|(19|2[0-9](0[48]|[2468][048]|[13579][26])))-02-29)|(((19|2[0-9])[0-9]{2})-02-(0[1-9]|1[0-9]|2[0-8]))|(((19|2[0-9])[0-9]{2})-(0[13578]|10|12)-(0[1-9]|[12][0-9]|3[01]))|(((19|2[0-9])[0-9]{2})-(0[469]|11)-(0[1-9]|[12][0-9]|30))T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\\.[0-9]+)?(Z|[+-][0-9]{2}:[0-9]{2})$"
}
```
- <a id='ssp-purpose'>**Purpose**</a>: Describes the purpose for the service within the system.
```json
{
  "title": "Purpose",
  "description": "Describes the purpose for the service within the system.",
  "$id": "#/definitions/purpose",
  "type": "string"
}
```
- <a id='ssp-remarks'>**Remarks**</a>: Additional commentary on the parent item.
```json
{
  "title": "Remarks",
  "description": "Additional commentary on the parent item.",
  "$id": "#/definitions/remarks",
  "type": "string"
}
```
- <a id='ssp-resource'>**Resource**</a>: A resource associated with the present document, which may be a pointer to other data or a citation.
```json
{
  "title": "Resource",
  "description": "A resource associated with the present document, which may be a pointer to other data or a citation.",
  "$id": "#/definitions/resource",
  "type": "object",
  "properties": {
    "uuid": {
      "title": "Universally Unique Identifier",
      "description": "A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "title": {
      "$ref": "#/definitions/title"
    },
    "desc": {
      "$ref": "#/definitions/desc"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "document-ids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/doc-id"
      }
    },
    "citation": {
      "$ref": "#/definitions/citation"
    },
    "rlinks": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/rlink"
      }
    },
    "attachments": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/base64"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "uuid"
  ],
  "additionalProperties": false
}
```
- <a id='ssp-responsible_party'>**Responsible Party**</a>: A reference to a set of organizations or persons that have responsibility for performing a referenced role relative to the parent context.
```json
{
  "title": "Responsible Party",
  "description": "A reference to a set of organizations or persons that have responsibility for performing a referenced role relative to the parent context.",
  "$id": "#/definitions/responsible-party",
  "type": "object",
  "properties": {
    "party-uuids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/party-uuid"
      }
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "party-uuids"
  ],
  "additionalProperties": false
}
```
- <a id='ssp-responsible_role'>**Responsible Role**</a>: A reference to one or more roles with responsibility for performing a function relative to the control.
```json
{
  "title": "Responsible Role",
  "description": "A reference to one or more roles with responsibility for performing a function relative to the control.",
  "$id": "#/definitions/responsible-role",
  "type": "object",
  "properties": {
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "party-ids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/party-uuid"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "additionalProperties": false
}
```
- <a id='ssp-revision_history_entry'>**Revision History Entry**</a>: An entry in a sequential list of revisions to the containing document in reverse chronological order (i.e., most recent previous revision first).
```json
{
  "title": "Revision History Entry",
  "description": "An entry in a sequential list of revisions to the containing document in reverse chronological order (i.e., most recent previous revision first).",
  "$id": "#/definitions/revision",
  "type": "object",
  "properties": {
    "title": {
      "$ref": "#/definitions/title"
    },
    "published": {
      "$ref": "#/definitions/published"
    },
    "last-modified": {
      "$ref": "#/definitions/last-modified"
    },
    "version": {
      "$ref": "#/definitions/version"
    },
    "oscal-version": {
      "$ref": "#/definitions/oscal-version"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "additionalProperties": false
}
```
- <a id='ssp-resource_link'>**Resource link**</a>: A pointer to an external copy of a document with optional hash for verification
```json
{
  "title": "Resource link",
  "description": "A pointer to an external copy of a document with optional hash for verification",
  "$id": "#/definitions/rlink",
  "type": "object",
  "properties": {
    "href": {
      "title": "hypertext reference",
      "description": "A link to a document or document fragment (actual, nominal or projected)",
      "type": "string",
      "format": "uri-reference"
    },
    "media-type": {
      "title": "Media type",
      "description": "Describes the media type of the linked resource",
      "type": "string"
    },
    "hashes": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/hash"
      }
    }
  },
  "required": [
    "href"
  ],
  "additionalProperties": false
}
```
- <a id='ssp-role'>**Role**</a>: Defining a role to be assigned to a party
```json
{
  "title": "Role",
  "description": "Defining a role to be assigned to a party",
  "$id": "#/definitions/role",
  "type": "object",
  "properties": {
    "id": {
      "title": "Identifier",
      "description": "Unique identifier of the containing object",
      "type": "string"
    },
    "title": {
      "$ref": "#/definitions/title"
    },
    "short-name": {
      "$ref": "#/definitions/short-name"
    },
    "desc": {
      "$ref": "#/definitions/desc"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "id",
    "title"
  ],
  "additionalProperties": false
}
```
- <a id='ssp-role_identifier_reference'>**Role Identifier Reference**</a>: A reference to the roles served by the user.
```json
{
  "title": "Role Identifier Reference",
  "description": "A reference to the roles served by the user.",
  "$id": "#/definitions/role-id",
  "type": "string"
}
```
- <a id='ssp-security_impact_level'>**Security Impact Level**</a>: The overall level of expected impact resulting from unauthorized disclosure, modification, or loss of access to information.
```json
{
  "title": "Security Impact Level",
  "description": "The overall level of expected impact resulting from unauthorized disclosure, modification, or loss of access to information.",
  "$id": "#/definitions/security-impact-level",
  "type": "object",
  "properties": {
    "security-objective-confidentiality": {
      "$ref": "#/definitions/security-objective-confidentiality"
    },
    "security-objective-integrity": {
      "$ref": "#/definitions/security-objective-integrity"
    },
    "security-objective-availability": {
      "$ref": "#/definitions/security-objective-availability"
    }
  },
  "additionalProperties": false
}
```
- <a id='ssp-security_objective:_availability'>**Security Objective: Availability**</a>: A target-level of availability for the system, based on the sensitivity of information within the system.
```json
{
  "title": "Security Objective: Availability",
  "description": "A target-level of availability for the system, based on the sensitivity of information within the system.",
  "$id": "#/definitions/security-objective-availability",
  "type": "string",
  "enum": [
    "fips-199-low",
    "fips-199-moderate",
    "fips-199-high"
  ]
}
```
- <a id='ssp-security_objective:_confidentiality'>**Security Objective: Confidentiality**</a>: A target-level of confidentiality for the system, based on the sensitivity of information within the system.
```json
{
  "title": "Security Objective: Confidentiality",
  "description": "A target-level of confidentiality for the system, based on the sensitivity of information within the system.",
  "$id": "#/definitions/security-objective-confidentiality",
  "type": "string",
  "enum": [
    "fips-199-low",
    "fips-199-moderate",
    "fips-199-high"
  ]
}
```
- <a id='ssp-security_objective:_integrity'>**Security Objective: Integrity**</a>: A target-level of integrity for the system, based on the sensitivity of information within the system.
```json
{
  "title": "Security Objective: Integrity",
  "description": "A target-level of integrity for the system, based on the sensitivity of information within the system.",
  "$id": "#/definitions/security-objective-integrity",
  "type": "string",
  "enum": [
    "fips-199-low",
    "fips-199-moderate",
    "fips-199-high"
  ]
}
```
- <a id='ssp-security_sensitivity_level'>**Security Sensitivity Level**</a>: The overall information system sensitivity categorization, such as defined by FIPS-199.
```json
{
  "title": "Security Sensitivity Level",
  "description": "The overall information system sensitivity categorization, such as defined by FIPS-199.",
  "$id": "#/definitions/security-sensitivity-level",
  "type": "string",
  "enum": [
    "low",
    "moderate",
    "high"
  ]
}
```
- <a id='ssp-selected_level_(confidentiality,_integrity,_or_availability)'>**Selected Level (Confidentiality, Integrity, or Availability)**</a>: The selected (Confidentiality, Integrity, or Availability) security impact level.
```json
{
  "title": "Selected Level (Confidentiality, Integrity, or Availability)",
  "description": "The selected (Confidentiality, Integrity, or Availability) security impact level.",
  "$id": "#/definitions/selected",
  "type": "string",
  "enum": [
    "fips-199-low",
    "fips-199-moderate",
    "fips-199-high"
  ]
}
```
- <a id='ssp-set_parameter_value'>**Set Parameter Value**</a>: Identifies the parameter that will be filled in by the enclosed value element.
```json
{
  "title": "Set Parameter Value",
  "description": "Identifies the parameter that will be filled in by the enclosed value element.",
  "$id": "#/definitions/set-parameter",
  "type": "object",
  "properties": {
    "value": {
      "$ref": "#/definitions/value"
    }
  },
  "required": [
    "value"
  ],
  "additionalProperties": false
}
```
- <a id='ssp-short-name'>**short-name**</a>: A common name, short name or acronym
```json
{
  "title": "short-name",
  "description": "A common name, short name or acronym",
  "$id": "#/definitions/short-name",
  "type": "string"
}
```
- <a id='ssp-state'>**State**</a>: State, province or analogous geographical region for mailing address
```json
{
  "title": "State",
  "description": "State, province or analogous geographical region for mailing address",
  "$id": "#/definitions/state",
  "type": "string"
}
```
- <a id='ssp-specific_statement'>**Specific Statement**</a>: Identifies which statements within a control are addressed.
```json
{
  "title": "Specific Statement",
  "description": "Identifies which statements within a control are addressed.",
  "$id": "#/definitions/statement",
  "type": "object",
  "properties": {
    "uuid": {
      "title": "Universally Unique Identifier",
      "description": "A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "description": {
      "$ref": "#/definitions/description"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "anyOf": [
        {
          "$ref": "#/definitions/annotation"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/annotation"
          },
          "minItems": 2
        }
      ]
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "responsible-roles": {
      "type": "object",
      "minProperties": 1,
      "additionalProperties": {
        "allOf": [
          {
            "type": "object",
            "$ref": "#/definitions/responsible-role"
          },
          {
            "not": {
              "type": "string"
            }
          }
        ]
      }
    },
    "by-components": {
      "type": "object",
      "minProperties": 1,
      "additionalProperties": {
        "allOf": [
          {
            "type": "object",
            "$ref": "#/definitions/by-component"
          },
          {
            "not": {
              "type": "string"
            }
          }
        ]
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "uuid"
  ],
  "additionalProperties": false
}
```
- <a id='ssp-status'>**Status**</a>: Describes the operational status of the system.
```json
{
  "title": "Status",
  "description": "Describes the operational status of the system.",
  "$id": "#/definitions/status",
  "type": "object",
  "properties": {
    "state": {
      "title": "State",
      "description": "The current operating status.",
      "type": "string",
      "enum": [
        "operational",
        "under-development",
        "under-major-modification",
        "disposition",
        "other"
      ]
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "state"
  ],
  "additionalProperties": false
}
```
- <a id='ssp-system_characteristics'>**System Characteristics**</a>: Contains the characteristics of the system, such as its name, purpose, and security impact level.
```json
{
  "title": "System Characteristics",
  "description": "Contains the characteristics of the system, such as its name, purpose, and security impact level.",
  "$id": "#/definitions/system-characteristics",
  "type": "object",
  "properties": {
    "system-ids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/system-id"
      }
    },
    "system-name": {
      "$ref": "#/definitions/system-name"
    },
    "system-name-short": {
      "$ref": "#/definitions/system-name-short"
    },
    "description": {
      "$ref": "#/definitions/description"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "date-authorized": {
      "$ref": "#/definitions/date-authorized"
    },
    "security-sensitivity-level": {
      "$ref": "#/definitions/security-sensitivity-level"
    },
    "system-information": {
      "$ref": "#/definitions/system-information"
    },
    "security-impact-level": {
      "$ref": "#/definitions/security-impact-level"
    },
    "status": {
      "$ref": "#/definitions/status"
    },
    "authorization-boundary": {
      "$ref": "#/definitions/authorization-boundary"
    },
    "network-architecture": {
      "$ref": "#/definitions/network-architecture"
    },
    "data-flow": {
      "$ref": "#/definitions/data-flow"
    },
    "responsible-parties": {
      "type": "object",
      "minProperties": 1,
      "additionalProperties": {
        "allOf": [
          {
            "type": "object",
            "$ref": "#/definitions/responsible-party"
          },
          {
            "not": {
              "type": "string"
            }
          }
        ]
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "system-ids",
    "system-name",
    "description",
    "security-sensitivity-level",
    "system-information",
    "security-impact-level",
    "status",
    "authorization-boundary"
  ],
  "additionalProperties": false
}
```
- <a id='ssp-system_identification'>**System Identification**</a>: A unique identifier for the system described by this system security plan.
```json
{
  "title": "System Identification",
  "description": "A unique identifier for the system described by this system security plan.",
  "$id": "#/definitions/system-id",
  "type": "object",
  "properties": {
    "identifier-type": {
      "title": "Identification System Type",
      "description": "Identifies the identification system from which the provided identifier was assigned.",
      "type": "string",
      "format": "uri"
    },
    "id": {
      "type": "string"
    }
  },
  "required": [
    "id"
  ],
  "additionalProperties": false
}
```
- <a id='ssp-system_implementation'>**System Implementation**</a>: Provides information as to how the system is implemented.
```json
{
  "title": "System Implementation",
  "description": "Provides information as to how the system is implemented.",
  "$id": "#/definitions/system-implementation",
  "type": "object",
  "properties": {
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "leveraged-authorizations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/leveraged-authorization"
      }
    },
    "users": {
      "type": "object",
      "minProperties": 1,
      "additionalProperties": {
        "allOf": [
          {
            "type": "object",
            "$ref": "#/definitions/user"
          },
          {
            "not": {
              "type": "string"
            }
          }
        ]
      }
    },
    "components": {
      "type": "object",
      "minProperties": 1,
      "additionalProperties": {
        "allOf": [
          {
            "type": "object",
            "$ref": "#/definitions/component"
          },
          {
            "not": {
              "type": "string"
            }
          }
        ]
      }
    },
    "system-inventory": {
      "$ref": "#/definitions/system-inventory"
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "users"
  ],
  "additionalProperties": false
}
```
- <a id='ssp-system_information'>**System Information**</a>: Contains details about all information types that are stored, processed, or transmitted by the system, such as privacy information, and those defined in NIST SP 800-60.
```json
{
  "title": "System Information",
  "description": "Contains details about all information types that are stored, processed, or transmitted by the system, such as privacy information, and those defined in NIST SP 800-60.",
  "$id": "#/definitions/system-information",
  "type": "object",
  "properties": {
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "information-types": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/information-type"
      }
    }
  },
  "required": [
    "information-types"
  ],
  "additionalProperties": false
}
```
- <a id='ssp-system_inventory'>**System Inventory**</a>: A set of inventory-item entries that represent the managed inventory instances of the system.
```json
{
  "title": "System Inventory",
  "description": "A set of inventory-item entries that represent the managed inventory instances of the system.",
  "$id": "#/definitions/system-inventory",
  "type": "object",
  "properties": {
    "inventory-items": {
      "type": "object",
      "minProperties": 1,
      "additionalProperties": {
        "allOf": [
          {
            "type": "object",
            "$ref": "#/definitions/inventory-item"
          },
          {
            "not": {
              "type": "string"
            }
          }
        ]
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "inventory-items"
  ],
  "additionalProperties": false
}
```
- <a id='ssp-system_name_(full)'>**System Name (Full)**</a>: The full name of the system.
```json
{
  "title": "System Name (Full)",
  "description": "The full name of the system.",
  "$id": "#/definitions/system-name",
  "type": "string"
}
```
- <a id='ssp-system_name_(short)'>**System Name (Short)**</a>: A short name for the system, such as an acronym, that is suitable for display in a data table or summary list.
```json
{
  "title": "System Name (Short)",
  "description": "A short name for the system, such as an acronym, that is suitable for display in a data table or summary list.",
  "$id": "#/definitions/system-name-short",
  "type": "string"
}
```
- <a id='ssp-system_security_plan_(ssp)'>**System Security Plan (SSP)**</a>: A system security plan, such as those described in NIST SP 800-18
```json
{
  "title": "System Security Plan (SSP)",
  "description": "A system security plan, such as those described in NIST SP 800-18",
  "$id": "#/definitions/system-security-plan",
  "type": "object",
  "properties": {
    "uuid": {
      "title": "Universally Unique Identifier",
      "description": "A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.",
      "type": "string",
      "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$"
    },
    "metadata": {
      "$ref": "#/definitions/metadata"
    },
    "import-profile": {
      "$ref": "#/definitions/import-profile"
    },
    "system-characteristics": {
      "$ref": "#/definitions/system-characteristics"
    },
    "system-implementation": {
      "$ref": "#/definitions/system-implementation"
    },
    "control-implementation": {
      "$ref": "#/definitions/control-implementation"
    },
    "back-matter": {
      "$ref": "#/definitions/back-matter"
    }
  },
  "required": [
    "uuid",
    "metadata",
    "import-profile",
    "system-characteristics",
    "system-implementation",
    "control-implementation"
  ],
  "additionalProperties": false
}
```
- <a id='ssp-text'>**Text**</a>: A line of textual content whose semantic is determined by the context of use.
```json
{
  "title": "Text",
  "description": "A line of textual content whose semantic is determined by the context of use.",
  "$id": "#/definitions/text",
  "type": "string"
}
```
- <a id='ssp-title'>**Title**</a>: A title for display and navigation
```json
{
  "title": "Title",
  "description": "A title for display and navigation",
  "$id": "#/definitions/title",
  "type": "string"
}
```
- <a id='ssp-url'>**URL**</a>: URL for web site or Internet presence
```json
{
  "title": "URL",
  "description": "URL for web site or Internet presence",
  "$id": "#/definitions/url",
  "type": "string",
  "format": "uri"
}
```
- <a id='ssp-system_user_class'>**System User Class**</a>: A type of user that interacts with the system based on an associated role.
```json
{
  "title": "System User Class",
  "description": "A type of user that interacts with the system based on an associated role.",
  "$id": "#/definitions/user",
  "type": "object",
  "properties": {
    "title": {
      "$ref": "#/definitions/title"
    },
    "short-name": {
      "$ref": "#/definitions/short-name"
    },
    "description": {
      "$ref": "#/definitions/description"
    },
    "properties": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/prop"
      }
    },
    "annotations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/annotation"
      }
    },
    "links": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/link"
      }
    },
    "role-ids": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/role-id"
      }
    },
    "authorized-privileges": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/authorized-privilege"
      }
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "role-ids"
  ],
  "additionalProperties": false
}
```
- <a id='ssp-value'>**Value**</a>: The phrase or string that fills-in the parameter and completes the requirement statement.
```json
{
  "title": "Value",
  "description": "The phrase or string that fills-in the parameter and completes the requirement statement.",
  "$id": "#/definitions/value",
  "type": "string"
}
```
- <a id='ssp-document_version'>**Document version**</a>: The version of the document content.
```json
{
  "title": "Document version",
  "description": "The version of the document content.",
  "$id": "#/definitions/version",
  "type": "string"
}
```


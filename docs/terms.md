## catalog

> OSCAL Control Catalog Format

- **Address line**: A single line of an address.
```json
{
  "title": "Address line",
  "description": "A single line of an address.",
  "$id": "#/definitions/addr-line",
  "type": "string"
}
```
- **Address**: A postal address.
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
      "anyOf": [
        {
          "$ref": "#/definitions/addr-line"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/addr-line"
          },
          "minItems": 2
        }
      ]
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
- **Annotation**: A name/value pair with optional explanatory remarks.
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
- **Back matter**: A collection of citations and resource references.
```json
{
  "title": "Back matter",
  "description": "A collection of citations and resource references.",
  "$id": "#/definitions/back-matter",
  "type": "object",
  "properties": {
    "citations": {
      "anyOf": [
        {
          "$ref": "#/definitions/citation"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/citation"
          },
          "minItems": 2
        }
      ]
    },
    "resources": {
      "anyOf": [
        {
          "$ref": "#/definitions/resource"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/resource"
          },
          "minItems": 2
        }
      ]
    }
  },
  "additionalProperties": false
}
```
- **Base64**: 
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
- **Catalog**: A collection of controls.
```json
{
  "title": "Catalog",
  "description": "A collection of controls.",
  "$id": "#/definitions/catalog",
  "type": "object",
  "properties": {
    "id": {
      "title": "Identifier",
      "description": "Unique identifier of the containing object",
      "type": "string"
    },
    "metadata": {
      "$ref": "#/definitions/metadata"
    },
    "groups": {
      "anyOf": [
        {
          "$ref": "#/definitions/group"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/group"
          },
          "minItems": 2
        }
      ]
    },
    "controls": {
      "anyOf": [
        {
          "$ref": "#/definitions/control"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/control"
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
    "id",
    "metadata"
  ],
  "additionalProperties": false
}
```
- **Choice**: A value selection among several such options
```json
{
  "title": "Choice",
  "description": "A value selection among several such options",
  "$id": "#/definitions/choice",
  "type": "string"
}
```
- **Citation**: A citation to resources, either external or internal (by means of internal cross-reference).
```json
{
  "title": "Citation",
  "description": "A citation to resources, either external or internal (by means of internal cross-reference).",
  "$id": "#/definitions/citation",
  "type": "object",
  "properties": {
    "id": {
      "title": "Identifier",
      "description": "Unique identifier of the containing object",
      "type": "string"
    },
    "targets": {
      "anyOf": [
        {
          "$ref": "#/definitions/target"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/target"
          },
          "minItems": 2
        }
      ]
    },
    "title": {
      "$ref": "#/definitions/title"
    },
    "desc": {
      "$ref": "#/definitions/desc"
    },
    "document-ids": {
      "anyOf": [
        {
          "$ref": "#/definitions/doc-id"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/doc-id"
          },
          "minItems": 2
        }
      ]
    },
    "properties": {
      "anyOf": [
        {
          "$ref": "#/definitions/prop"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/prop"
          },
          "minItems": 2
        }
      ]
    }
  },
  "required": [
    "id"
  ],
  "additionalProperties": false
}
```
- **City**: City, town or geographical region for mailing address
```json
{
  "title": "City",
  "description": "City, town or geographical region for mailing address",
  "$id": "#/definitions/city",
  "type": "string"
}
```
- **Constraint**: A formal or informal expression of a constraint or test
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
- **Control**: A structured information object representing a security or privacy control. Each security or privacy control within the Catalog is defined by a distinct control instance.
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
      "anyOf": [
        {
          "$ref": "#/definitions/param"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/param"
          },
          "minItems": 2
        }
      ]
    },
    "properties": {
      "anyOf": [
        {
          "$ref": "#/definitions/prop"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/prop"
          },
          "minItems": 2
        }
      ]
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
      "anyOf": [
        {
          "$ref": "#/definitions/link"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/link"
          },
          "minItems": 2
        }
      ]
    },
    "parts": {
      "anyOf": [
        {
          "$ref": "#/definitions/part"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/part"
          },
          "minItems": 2
        }
      ]
    },
    "controls": {
      "anyOf": [
        {
          "$ref": "#/definitions/control"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/control"
          },
          "minItems": 2
        }
      ]
    }
  },
  "required": [
    "id",
    "title"
  ],
  "additionalProperties": false
}
```
- **Country**: Country for mailing address
```json
{
  "title": "Country",
  "description": "Country for mailing address",
  "$id": "#/definitions/country",
  "type": "string"
}
```
- **Description**: A short textual description
```json
{
  "title": "Description",
  "description": "A short textual description",
  "$id": "#/definitions/desc",
  "type": "string"
}
```
- **Document Identifier**: A document identifier qualified by an identifier type.
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
- **Email**: Email address
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
- **Control Group**: A group of controls, or of groups of controls.
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
      "anyOf": [
        {
          "$ref": "#/definitions/param"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/param"
          },
          "minItems": 2
        }
      ]
    },
    "properties": {
      "anyOf": [
        {
          "$ref": "#/definitions/prop"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/prop"
          },
          "minItems": 2
        }
      ]
    },
    "parts": {
      "anyOf": [
        {
          "$ref": "#/definitions/part"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/part"
          },
          "minItems": 2
        }
      ]
    },
    "groups": {
      "anyOf": [
        {
          "$ref": "#/definitions/group"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/group"
          },
          "minItems": 2
        }
      ]
    },
    "controls": {
      "anyOf": [
        {
          "$ref": "#/definitions/control"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/control"
          },
          "minItems": 2
        }
      ]
    }
  },
  "required": [
    "title"
  ],
  "additionalProperties": false
}
```
- **Guideline**: A prose statement that provides a recommendation for the use of a parameter.
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
- **Hash**: A representation of a cryptographic digest generated over a resource using a hash algorithm.
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
- **Parameter label**: A placeholder for a missing value, in display.
```json
{
  "title": "Parameter label",
  "description": "A placeholder for a missing value, in display.",
  "$id": "#/definitions/label",
  "type": "string"
}
```
- **Last modified timestamp**: Date and time of last modification.
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
- **Link**: A reference to a local or remote resource
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
- **Publication metadata**: Provides information about the publication and availability of the containing document.
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
    "document-ids": {
      "anyOf": [
        {
          "$ref": "#/definitions/doc-id"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/doc-id"
          },
          "minItems": 2
        }
      ]
    },
    "properties": {
      "anyOf": [
        {
          "$ref": "#/definitions/prop"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/prop"
          },
          "minItems": 2
        }
      ]
    },
    "links": {
      "anyOf": [
        {
          "$ref": "#/definitions/link"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/link"
          },
          "minItems": 2
        }
      ]
    },
    "roles": {
      "anyOf": [
        {
          "$ref": "#/definitions/role"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/role"
          },
          "minItems": 2
        }
      ]
    },
    "parties": {
      "anyOf": [
        {
          "$ref": "#/definitions/party"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/party"
          },
          "minItems": 2
        }
      ]
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
- **Organization**: An organization or legal entity (not a person), with contact information
```json
{
  "title": "Organization",
  "description": "An organization or legal entity (not a person), with contact information",
  "$id": "#/definitions/org",
  "type": "object",
  "properties": {
    "org-name": {
      "$ref": "#/definitions/org-name"
    },
    "short-name": {
      "$ref": "#/definitions/short-name"
    },
    "organization-ids": {
      "anyOf": [
        {
          "$ref": "#/definitions/org-id"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/org-id"
          },
          "minItems": 2
        }
      ]
    },
    "addresses": {
      "anyOf": [
        {
          "$ref": "#/definitions/address"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/address"
          },
          "minItems": 2
        }
      ]
    },
    "email-addresses": {
      "anyOf": [
        {
          "$ref": "#/definitions/email"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/email"
          },
          "minItems": 2
        }
      ]
    },
    "telephone-numbers": {
      "anyOf": [
        {
          "$ref": "#/definitions/phone"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/phone"
          },
          "minItems": 2
        }
      ]
    },
    "URLs": {
      "anyOf": [
        {
          "$ref": "#/definitions/url"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/url"
          },
          "minItems": 2
        }
      ]
    },
    "properties": {
      "anyOf": [
        {
          "$ref": "#/definitions/prop"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/prop"
          },
          "minItems": 2
        }
      ]
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
      "anyOf": [
        {
          "$ref": "#/definitions/link"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/link"
          },
          "minItems": 2
        }
      ]
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "org-name"
  ],
  "additionalProperties": false
}
```
- **Organization Identifier**: An identifier for an organization using a designated scheme.
```json
{
  "title": "Organization Identifier",
  "description": "An identifier for an organization using a designated scheme.",
  "$id": "#/definitions/org-id",
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
    "id"
  ],
  "additionalProperties": false
}
```
- **Organization Name**: Full (legal) name of an organization
```json
{
  "title": "Organization Name",
  "description": "Full (legal) name of an organization",
  "$id": "#/definitions/org-name",
  "type": "string"
}
```
- **OSCAL version**: OSCAL model version.
```json
{
  "title": "OSCAL version",
  "description": "OSCAL model version.",
  "$id": "#/definitions/oscal-version",
  "type": "string"
}
```
- **Parameter**: Parameters provide a mechanism for the dynamic assignment of value(s) in a control.
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
      "anyOf": [
        {
          "$ref": "#/definitions/usage"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/usage"
          },
          "minItems": 2
        }
      ]
    },
    "constraints": {
      "anyOf": [
        {
          "$ref": "#/definitions/constraint"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/constraint"
          },
          "minItems": 2
        }
      ]
    },
    "guidance": {
      "anyOf": [
        {
          "$ref": "#/definitions/guideline"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/guideline"
          },
          "minItems": 2
        }
      ]
    },
    "value": {
      "$ref": "#/definitions/value"
    },
    "select": {
      "$ref": "#/definitions/select"
    },
    "links": {
      "anyOf": [
        {
          "$ref": "#/definitions/link"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/link"
          },
          "minItems": 2
        }
      ]
    }
  },
  "required": [
    "id"
  ],
  "additionalProperties": false
}
```
- **Part**: A partition or component of a control or part
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
      "anyOf": [
        {
          "$ref": "#/definitions/prop"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/prop"
          },
          "minItems": 2
        }
      ]
    },
    "prose": {
      "$ref": "#/definitions/prose"
    },
    "parts": {
      "anyOf": [
        {
          "$ref": "#/definitions/part"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/part"
          },
          "minItems": 2
        }
      ]
    },
    "links": {
      "anyOf": [
        {
          "$ref": "#/definitions/link"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/link"
          },
          "minItems": 2
        }
      ]
    }
  },
  "required": [
    "name"
  ],
  "additionalProperties": false
}
```
- **Party (organization or person)**: A responsible entity, either singular (an organization or person) or collective (multiple persons)
```json
{
  "title": "Party (organization or person)",
  "description": "A responsible entity, either singular (an organization or person) or collective (multiple persons)",
  "$id": "#/definitions/party",
  "type": "object",
  "properties": {
    "id": {
      "title": "Identifier",
      "description": "Unique identifier of the containing object",
      "type": "string"
    },
    "persons": {
      "anyOf": [
        {
          "$ref": "#/definitions/person"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/person"
          },
          "minItems": 2
        }
      ]
    },
    "org": {
      "$ref": "#/definitions/org"
    },
    "properties": {
      "anyOf": [
        {
          "$ref": "#/definitions/prop"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/prop"
          },
          "minItems": 2
        }
      ]
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
      "anyOf": [
        {
          "$ref": "#/definitions/link"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/link"
          },
          "minItems": 2
        }
      ]
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "additionalProperties": false
}
```
- **Party Reference**: References a party defined in metadata.
```json
{
  "title": "Party Reference",
  "description": "References a party defined in metadata.",
  "$id": "#/definitions/party-id",
  "type": "string"
}
```
- **Person**: A person, with contact information
```json
{
  "title": "Person",
  "description": "A person, with contact information",
  "$id": "#/definitions/person",
  "type": "object",
  "properties": {
    "person-name": {
      "$ref": "#/definitions/person-name"
    },
    "short-name": {
      "$ref": "#/definitions/short-name"
    },
    "org-name": {
      "$ref": "#/definitions/org-name"
    },
    "person-ids": {
      "anyOf": [
        {
          "$ref": "#/definitions/person-id"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/person-id"
          },
          "minItems": 2
        }
      ]
    },
    "organization-ids": {
      "anyOf": [
        {
          "$ref": "#/definitions/org-id"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/org-id"
          },
          "minItems": 2
        }
      ]
    },
    "addresses": {
      "anyOf": [
        {
          "$ref": "#/definitions/address"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/address"
          },
          "minItems": 2
        }
      ]
    },
    "email-addresses": {
      "anyOf": [
        {
          "$ref": "#/definitions/email"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/email"
          },
          "minItems": 2
        }
      ]
    },
    "telephone-numbers": {
      "anyOf": [
        {
          "$ref": "#/definitions/phone"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/phone"
          },
          "minItems": 2
        }
      ]
    },
    "URLs": {
      "anyOf": [
        {
          "$ref": "#/definitions/url"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/url"
          },
          "minItems": 2
        }
      ]
    },
    "properties": {
      "anyOf": [
        {
          "$ref": "#/definitions/prop"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/prop"
          },
          "minItems": 2
        }
      ]
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
      "anyOf": [
        {
          "$ref": "#/definitions/link"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/link"
          },
          "minItems": 2
        }
      ]
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "additionalProperties": false
}
```
- **Personal Identifier**: An identifier for a person (such as an ORCID) using a designated scheme.
```json
{
  "title": "Personal Identifier",
  "description": "An identifier for a person (such as an ORCID) using a designated scheme.",
  "$id": "#/definitions/person-id",
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
    "id"
  ],
  "additionalProperties": false
}
```
- **Person Name**: Full (legal) name of an individual
```json
{
  "title": "Person Name",
  "description": "Full (legal) name of an individual",
  "$id": "#/definitions/person-name",
  "type": "string"
}
```
- **Telephone**: Contact number by telephone
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
- **Postal Code**: Postal or ZIP code for mailing address
```json
{
  "title": "Postal Code",
  "description": "Postal or ZIP code for mailing address",
  "$id": "#/definitions/postal-code",
  "type": "string"
}
```
- **Property**: A value with a name, attributed to the containing control, part, or group.
```json
{
  "title": "Property",
  "description": "A value with a name, attributed to the containing control, part, or group.",
  "$id": "#/definitions/prop",
  "type": "object",
  "properties": {
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
    }
  },
  "minProperties": 1,
  "maxProperties": 4
}
```
- **Prose**: Prose permits multiple paragraphs, lists, tables etc.
```json
{
  "title": "Prose",
  "description": "Prose permits multiple paragraphs, lists, tables etc.",
  "$id": "#/definitions/prose",
  "type": "string"
}
```
- **Publication Timestamp**: The date and time this document was published.
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
- **Remarks**: Additional commentary on the parent item.
```json
{
  "title": "Remarks",
  "description": "Additional commentary on the parent item.",
  "$id": "#/definitions/remarks",
  "type": "string"
}
```
- **Resource**: A resource associated with the present document.
```json
{
  "title": "Resource",
  "description": "A resource associated with the present document.",
  "$id": "#/definitions/resource",
  "type": "object",
  "properties": {
    "id": {
      "title": "Identifier",
      "description": "Unique identifier of the containing object",
      "type": "string"
    },
    "desc": {
      "$ref": "#/definitions/desc"
    },
    "properties": {
      "anyOf": [
        {
          "$ref": "#/definitions/prop"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/prop"
          },
          "minItems": 2
        }
      ]
    },
    "rlinks": {
      "anyOf": [
        {
          "$ref": "#/definitions/rlink"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/rlink"
          },
          "minItems": 2
        }
      ]
    },
    "base64": {
      "$ref": "#/definitions/base64"
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "id"
  ],
  "additionalProperties": false
}
```
- **Responsible Party**: A reference to a set of organizations or persons that have responsibility for performing a referenced role relative to the parent context.
```json
{
  "title": "Responsible Party",
  "description": "A reference to a set of organizations or persons that have responsibility for performing a referenced role relative to the parent context.",
  "$id": "#/definitions/responsible-party",
  "type": "object",
  "properties": {
    "party-ids": {
      "anyOf": [
        {
          "$ref": "#/definitions/party-id"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/party-id"
          },
          "minItems": 2
        }
      ]
    },
    "properties": {
      "anyOf": [
        {
          "$ref": "#/definitions/prop"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/prop"
          },
          "minItems": 2
        }
      ]
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
      "anyOf": [
        {
          "$ref": "#/definitions/link"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/link"
          },
          "minItems": 2
        }
      ]
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "party-ids"
  ],
  "additionalProperties": false
}
```
- **Resource link**: A pointer to an external copy of a document with optional hash for verification
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
      "anyOf": [
        {
          "$ref": "#/definitions/hash"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/hash"
          },
          "minItems": 2
        }
      ]
    }
  },
  "required": [
    "href"
  ],
  "additionalProperties": false
}
```
- **Role**: Defining a role to be assigned to a party
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
      "anyOf": [
        {
          "$ref": "#/definitions/prop"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/prop"
          },
          "minItems": 2
        }
      ]
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
      "anyOf": [
        {
          "$ref": "#/definitions/link"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/link"
          },
          "minItems": 2
        }
      ]
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
- **Selection**: Presenting a choice among alternatives
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
      "anyOf": [
        {
          "$ref": "#/definitions/choice"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/choice"
          },
          "minItems": 2
        }
      ]
    }
  },
  "additionalProperties": false
}
```
- **short-name**: A common name, short name or acronym
```json
{
  "title": "short-name",
  "description": "A common name, short name or acronym",
  "$id": "#/definitions/short-name",
  "type": "string"
}
```
- **State**: State, province or analogous geographical region for mailing address
```json
{
  "title": "State",
  "description": "State, province or analogous geographical region for mailing address",
  "$id": "#/definitions/state",
  "type": "string"
}
```
- **Citation target**: An address for retrieval of a citation
```json
{
  "title": "Citation target",
  "description": "An address for retrieval of a citation",
  "$id": "#/definitions/target",
  "type": "string"
}
```
- **Title**: A title for display and navigation
```json
{
  "title": "Title",
  "description": "A title for display and navigation",
  "$id": "#/definitions/title",
  "type": "string"
}
```
- **URL**: URL for web site or Internet presence
```json
{
  "title": "URL",
  "description": "URL for web site or Internet presence",
  "$id": "#/definitions/url",
  "type": "string",
  "format": "uri"
}
```
- **Parameter description**: Indicates and explains the purpose and use of a parameter
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
- **Value constraint**: Indicates a permissible value for a parameter or property
```json
{
  "title": "Value constraint",
  "description": "Indicates a permissible value for a parameter or property",
  "$id": "#/definitions/value",
  "type": "string"
}
```
- **Document version**: The version of the document content.
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

- **Address line**: A single line of an address.
```json
{
  "title": "Address line",
  "description": "A single line of an address.",
  "$id": "#/definitions/addr-line",
  "type": "string"
}
```
- **Address**: A postal address.
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
      "anyOf": [
        {
          "$ref": "#/definitions/addr-line"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/addr-line"
          },
          "minItems": 2
        }
      ]
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
- **Annotation**: A name/value pair with optional explanatory remarks.
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
- **Back matter**: A collection of citations and resource references.
```json
{
  "title": "Back matter",
  "description": "A collection of citations and resource references.",
  "$id": "#/definitions/back-matter",
  "type": "object",
  "properties": {
    "citations": {
      "anyOf": [
        {
          "$ref": "#/definitions/citation"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/citation"
          },
          "minItems": 2
        }
      ]
    },
    "resources": {
      "anyOf": [
        {
          "$ref": "#/definitions/resource"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/resource"
          },
          "minItems": 2
        }
      ]
    }
  },
  "additionalProperties": false
}
```
- **Base64**: 
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
- **Can Meet**: Defines what sets of controls are supported by the component.
```json
{
  "title": "Can Meet",
  "description": "Defines what sets of controls are supported by the component.",
  "$id": "#/definitions/can-meet-requirement-set",
  "type": "object",
  "properties": {
    "source": {
      "title": "Source Resource Reference",
      "description": "A reference to an OSCAL catalog or profile providing the referenced control or subcontrol definition.",
      "type": "string",
      "format": "uri-reference"
    },
    "description": {
      "$ref": "#/definitions/description"
    },
    "properties": {
      "anyOf": [
        {
          "$ref": "#/definitions/prop"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/prop"
          },
          "minItems": 2
        }
      ]
    },
    "links": {
      "anyOf": [
        {
          "$ref": "#/definitions/link"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/link"
          },
          "minItems": 2
        }
      ]
    },
    "implemented-requirements": {
      "anyOf": [
        {
          "$ref": "#/definitions/implemented-requirement"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/implemented-requirement"
          },
          "minItems": 2
        }
      ]
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "source",
    "description",
    "implemented-requirements"
  ],
  "additionalProperties": false
}
```
- **Capability**: A grouping of other components and/or capabilities.
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
      "anyOf": [
        {
          "$ref": "#/definitions/prop"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/prop"
          },
          "minItems": 2
        }
      ]
    },
    "links": {
      "anyOf": [
        {
          "$ref": "#/definitions/link"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/link"
          },
          "minItems": 2
        }
      ]
    },
    "incorporates-capabilities": {
      "type": "object",
      "minProperties": 1,
      "additionalProperties": {
        "allOf": [
          {
            "type": "object",
            "$ref": "#/definitions/incorporates-capability"
          },
          {
            "not": {
              "type": "string"
            }
          }
        ]
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
      "anyOf": [
        {
          "$ref": "#/definitions/control-implementation"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/control-implementation"
          },
          "minItems": 2
        }
      ]
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
- **Citation**: A citation to resources, either external or internal (by means of internal cross-reference).
```json
{
  "title": "Citation",
  "description": "A citation to resources, either external or internal (by means of internal cross-reference).",
  "$id": "#/definitions/citation",
  "type": "object",
  "properties": {
    "id": {
      "title": "Identifier",
      "description": "Unique identifier of the containing object",
      "type": "string"
    },
    "targets": {
      "anyOf": [
        {
          "$ref": "#/definitions/target"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/target"
          },
          "minItems": 2
        }
      ]
    },
    "title": {
      "$ref": "#/definitions/title"
    },
    "desc": {
      "$ref": "#/definitions/desc"
    },
    "document-ids": {
      "anyOf": [
        {
          "$ref": "#/definitions/doc-id"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/doc-id"
          },
          "minItems": 2
        }
      ]
    },
    "properties": {
      "anyOf": [
        {
          "$ref": "#/definitions/prop"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/prop"
          },
          "minItems": 2
        }
      ]
    }
  },
  "required": [
    "id"
  ],
  "additionalProperties": false
}
```
- **City**: City, town or geographical region for mailing address
```json
{
  "title": "City",
  "description": "City, town or geographical region for mailing address",
  "$id": "#/definitions/city",
  "type": "string"
}
```
- **Component**: A defined component that can be part of an implemented system.
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
      "anyOf": [
        {
          "$ref": "#/definitions/prop"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/prop"
          },
          "minItems": 2
        }
      ]
    },
    "links": {
      "anyOf": [
        {
          "$ref": "#/definitions/link"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/link"
          },
          "minItems": 2
        }
      ]
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
      "anyOf": [
        {
          "$ref": "#/definitions/control-implementation"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/control-implementation"
          },
          "minItems": 2
        }
      ]
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
- **Component Definition**: TBD
```json
{
  "title": "Component Definition",
  "description": "TBD",
  "$id": "#/definitions/component-definition",
  "type": "object",
  "properties": {
    "metadata": {
      "$ref": "#/definitions/metadata"
    },
    "import-component-definitions": {
      "anyOf": [
        {
          "$ref": "#/definitions/import-component-definition"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/import-component-definition"
          },
          "minItems": 2
        }
      ]
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
- **Control Implementation**: Defines how the component or capability supports a set of controls.
```json
{
  "title": "Control Implementation",
  "description": "Defines how the component or capability supports a set of controls.",
  "$id": "#/definitions/control-implementation",
  "type": "object",
  "properties": {
    "description": {
      "$ref": "#/definitions/description"
    },
    "can-meet-requirement-sets": {
      "anyOf": [
        {
          "$ref": "#/definitions/can-meet-requirement-set"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/can-meet-requirement-set"
          },
          "minItems": 2
        }
      ]
    }
  },
  "required": [
    "description"
  ],
  "additionalProperties": false
}
```
- **Country**: Country for mailing address
```json
{
  "title": "Country",
  "description": "Country for mailing address",
  "$id": "#/definitions/country",
  "type": "string"
}
```
- **Description**: A short textual description
```json
{
  "title": "Description",
  "description": "A short textual description",
  "$id": "#/definitions/desc",
  "type": "string"
}
```
- **Description**: A description supporting the parent item.
```json
{
  "title": "Description",
  "description": "A description supporting the parent item.",
  "$id": "#/definitions/description",
  "type": "string"
}
```
- **Document Identifier**: A document identifier qualified by an identifier type.
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
- **Email**: Email address
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
- **Hash**: A representation of a cryptographic digest generated over a resource using a hash algorithm.
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
- **Control-based Requirement**: TBD
```json
{
  "title": "Control-based Requirement",
  "description": "TBD",
  "$id": "#/definitions/implemented-requirement",
  "type": "object",
  "properties": {
    "requirement-id": {
      "title": "Requirement Identifier Reference",
      "description": "A reference to a requirement defined on another requirement set that should be included here.",
      "type": "string"
    },
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
    "only-statements": {
      "type": "object",
      "minProperties": 1,
      "additionalProperties": {
        "allOf": [
          {
            "type": "object",
            "$ref": "#/definitions/only-statement"
          },
          {
            "not": {
              "type": "string"
            }
          }
        ]
      }
    },
    "description": {
      "$ref": "#/definitions/description"
    },
    "properties": {
      "anyOf": [
        {
          "$ref": "#/definitions/prop"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/prop"
          },
          "minItems": 2
        }
      ]
    },
    "links": {
      "anyOf": [
        {
          "$ref": "#/definitions/link"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/link"
          },
          "minItems": 2
        }
      ]
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "additionalProperties": false
}
```
- **Import Component Definition**: Loads a component definition from another resource.
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
- **Incorporates Capability**: TBD
```json
{
  "title": "Incorporates Capability",
  "description": "TBD",
  "$id": "#/definitions/incorporates-capability",
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
- **Incorporates Component**: TBD
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
- **Last modified timestamp**: Date and time of last modification.
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
- **Link**: A reference to a local or remote resource
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
- **Publication metadata**: Provides information about the publication and availability of the containing document.
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
    "document-ids": {
      "anyOf": [
        {
          "$ref": "#/definitions/doc-id"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/doc-id"
          },
          "minItems": 2
        }
      ]
    },
    "properties": {
      "anyOf": [
        {
          "$ref": "#/definitions/prop"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/prop"
          },
          "minItems": 2
        }
      ]
    },
    "links": {
      "anyOf": [
        {
          "$ref": "#/definitions/link"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/link"
          },
          "minItems": 2
        }
      ]
    },
    "roles": {
      "anyOf": [
        {
          "$ref": "#/definitions/role"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/role"
          },
          "minItems": 2
        }
      ]
    },
    "parties": {
      "anyOf": [
        {
          "$ref": "#/definitions/party"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/party"
          },
          "minItems": 2
        }
      ]
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
- **Specific Statement**: Describes which specific statements are addressed by a requirement, by pointing to a specific requirement statement within a control.
```json
{
  "title": "Specific Statement",
  "description": "Describes which specific statements are addressed by a requirement, by pointing to a specific requirement statement within a control.",
  "$id": "#/definitions/only-statement",
  "type": "object",
  "properties": {
    "description": {
      "$ref": "#/definitions/description"
    },
    "properties": {
      "anyOf": [
        {
          "$ref": "#/definitions/prop"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/prop"
          },
          "minItems": 2
        }
      ]
    },
    "links": {
      "anyOf": [
        {
          "$ref": "#/definitions/link"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/link"
          },
          "minItems": 2
        }
      ]
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "additionalProperties": false
}
```
- **Organization**: An organization or legal entity (not a person), with contact information
```json
{
  "title": "Organization",
  "description": "An organization or legal entity (not a person), with contact information",
  "$id": "#/definitions/org",
  "type": "object",
  "properties": {
    "org-name": {
      "$ref": "#/definitions/org-name"
    },
    "short-name": {
      "$ref": "#/definitions/short-name"
    },
    "organization-ids": {
      "anyOf": [
        {
          "$ref": "#/definitions/org-id"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/org-id"
          },
          "minItems": 2
        }
      ]
    },
    "addresses": {
      "anyOf": [
        {
          "$ref": "#/definitions/address"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/address"
          },
          "minItems": 2
        }
      ]
    },
    "email-addresses": {
      "anyOf": [
        {
          "$ref": "#/definitions/email"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/email"
          },
          "minItems": 2
        }
      ]
    },
    "telephone-numbers": {
      "anyOf": [
        {
          "$ref": "#/definitions/phone"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/phone"
          },
          "minItems": 2
        }
      ]
    },
    "URLs": {
      "anyOf": [
        {
          "$ref": "#/definitions/url"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/url"
          },
          "minItems": 2
        }
      ]
    },
    "properties": {
      "anyOf": [
        {
          "$ref": "#/definitions/prop"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/prop"
          },
          "minItems": 2
        }
      ]
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
      "anyOf": [
        {
          "$ref": "#/definitions/link"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/link"
          },
          "minItems": 2
        }
      ]
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "org-name"
  ],
  "additionalProperties": false
}
```
- **Organization Identifier**: An identifier for an organization using a designated scheme.
```json
{
  "title": "Organization Identifier",
  "description": "An identifier for an organization using a designated scheme.",
  "$id": "#/definitions/org-id",
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
    "id"
  ],
  "additionalProperties": false
}
```
- **Organization Name**: Full (legal) name of an organization
```json
{
  "title": "Organization Name",
  "description": "Full (legal) name of an organization",
  "$id": "#/definitions/org-name",
  "type": "string"
}
```
- **OSCAL version**: OSCAL model version.
```json
{
  "title": "OSCAL version",
  "description": "OSCAL model version.",
  "$id": "#/definitions/oscal-version",
  "type": "string"
}
```
- **Party (organization or person)**: A responsible entity, either singular (an organization or person) or collective (multiple persons)
```json
{
  "title": "Party (organization or person)",
  "description": "A responsible entity, either singular (an organization or person) or collective (multiple persons)",
  "$id": "#/definitions/party",
  "type": "object",
  "properties": {
    "id": {
      "title": "Identifier",
      "description": "Unique identifier of the containing object",
      "type": "string"
    },
    "persons": {
      "anyOf": [
        {
          "$ref": "#/definitions/person"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/person"
          },
          "minItems": 2
        }
      ]
    },
    "org": {
      "$ref": "#/definitions/org"
    },
    "properties": {
      "anyOf": [
        {
          "$ref": "#/definitions/prop"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/prop"
          },
          "minItems": 2
        }
      ]
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
      "anyOf": [
        {
          "$ref": "#/definitions/link"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/link"
          },
          "minItems": 2
        }
      ]
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "additionalProperties": false
}
```
- **Party Reference**: References a party defined in metadata.
```json
{
  "title": "Party Reference",
  "description": "References a party defined in metadata.",
  "$id": "#/definitions/party-id",
  "type": "string"
}
```
- **Person**: A person, with contact information
```json
{
  "title": "Person",
  "description": "A person, with contact information",
  "$id": "#/definitions/person",
  "type": "object",
  "properties": {
    "person-name": {
      "$ref": "#/definitions/person-name"
    },
    "short-name": {
      "$ref": "#/definitions/short-name"
    },
    "org-name": {
      "$ref": "#/definitions/org-name"
    },
    "person-ids": {
      "anyOf": [
        {
          "$ref": "#/definitions/person-id"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/person-id"
          },
          "minItems": 2
        }
      ]
    },
    "organization-ids": {
      "anyOf": [
        {
          "$ref": "#/definitions/org-id"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/org-id"
          },
          "minItems": 2
        }
      ]
    },
    "addresses": {
      "anyOf": [
        {
          "$ref": "#/definitions/address"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/address"
          },
          "minItems": 2
        }
      ]
    },
    "email-addresses": {
      "anyOf": [
        {
          "$ref": "#/definitions/email"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/email"
          },
          "minItems": 2
        }
      ]
    },
    "telephone-numbers": {
      "anyOf": [
        {
          "$ref": "#/definitions/phone"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/phone"
          },
          "minItems": 2
        }
      ]
    },
    "URLs": {
      "anyOf": [
        {
          "$ref": "#/definitions/url"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/url"
          },
          "minItems": 2
        }
      ]
    },
    "properties": {
      "anyOf": [
        {
          "$ref": "#/definitions/prop"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/prop"
          },
          "minItems": 2
        }
      ]
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
      "anyOf": [
        {
          "$ref": "#/definitions/link"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/link"
          },
          "minItems": 2
        }
      ]
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "additionalProperties": false
}
```
- **Personal Identifier**: An identifier for a person (such as an ORCID) using a designated scheme.
```json
{
  "title": "Personal Identifier",
  "description": "An identifier for a person (such as an ORCID) using a designated scheme.",
  "$id": "#/definitions/person-id",
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
    "id"
  ],
  "additionalProperties": false
}
```
- **Person Name**: Full (legal) name of an individual
```json
{
  "title": "Person Name",
  "description": "Full (legal) name of an individual",
  "$id": "#/definitions/person-name",
  "type": "string"
}
```
- **Telephone**: Contact number by telephone
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
- **Postal Code**: Postal or ZIP code for mailing address
```json
{
  "title": "Postal Code",
  "description": "Postal or ZIP code for mailing address",
  "$id": "#/definitions/postal-code",
  "type": "string"
}
```
- **Property**: A value with a name, attributed to the containing control, part, or group.
```json
{
  "title": "Property",
  "description": "A value with a name, attributed to the containing control, part, or group.",
  "$id": "#/definitions/prop",
  "type": "object",
  "properties": {
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
    }
  },
  "minProperties": 1,
  "maxProperties": 4
}
```
- **Publication Timestamp**: The date and time this document was published.
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
- **Remarks**: Additional commentary on the parent item.
```json
{
  "title": "Remarks",
  "description": "Additional commentary on the parent item.",
  "$id": "#/definitions/remarks",
  "type": "string"
}
```
- **Resource**: A resource associated with the present document.
```json
{
  "title": "Resource",
  "description": "A resource associated with the present document.",
  "$id": "#/definitions/resource",
  "type": "object",
  "properties": {
    "id": {
      "title": "Identifier",
      "description": "Unique identifier of the containing object",
      "type": "string"
    },
    "desc": {
      "$ref": "#/definitions/desc"
    },
    "properties": {
      "anyOf": [
        {
          "$ref": "#/definitions/prop"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/prop"
          },
          "minItems": 2
        }
      ]
    },
    "rlinks": {
      "anyOf": [
        {
          "$ref": "#/definitions/rlink"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/rlink"
          },
          "minItems": 2
        }
      ]
    },
    "base64": {
      "$ref": "#/definitions/base64"
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "id"
  ],
  "additionalProperties": false
}
```
- **Responsible Party**: A reference to a set of organizations or persons that have responsibility for performing a referenced role relative to the parent context.
```json
{
  "title": "Responsible Party",
  "description": "A reference to a set of organizations or persons that have responsibility for performing a referenced role relative to the parent context.",
  "$id": "#/definitions/responsible-party",
  "type": "object",
  "properties": {
    "party-ids": {
      "anyOf": [
        {
          "$ref": "#/definitions/party-id"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/party-id"
          },
          "minItems": 2
        }
      ]
    },
    "properties": {
      "anyOf": [
        {
          "$ref": "#/definitions/prop"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/prop"
          },
          "minItems": 2
        }
      ]
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
      "anyOf": [
        {
          "$ref": "#/definitions/link"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/link"
          },
          "minItems": 2
        }
      ]
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "party-ids"
  ],
  "additionalProperties": false
}
```
- **Resource link**: A pointer to an external copy of a document with optional hash for verification
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
      "anyOf": [
        {
          "$ref": "#/definitions/hash"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/hash"
          },
          "minItems": 2
        }
      ]
    }
  },
  "required": [
    "href"
  ],
  "additionalProperties": false
}
```
- **Role**: Defining a role to be assigned to a party
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
      "anyOf": [
        {
          "$ref": "#/definitions/prop"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/prop"
          },
          "minItems": 2
        }
      ]
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
      "anyOf": [
        {
          "$ref": "#/definitions/link"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/link"
          },
          "minItems": 2
        }
      ]
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
- **short-name**: A common name, short name or acronym
```json
{
  "title": "short-name",
  "description": "A common name, short name or acronym",
  "$id": "#/definitions/short-name",
  "type": "string"
}
```
- **State**: State, province or analogous geographical region for mailing address
```json
{
  "title": "State",
  "description": "State, province or analogous geographical region for mailing address",
  "$id": "#/definitions/state",
  "type": "string"
}
```
- **Citation target**: An address for retrieval of a citation
```json
{
  "title": "Citation target",
  "description": "An address for retrieval of a citation",
  "$id": "#/definitions/target",
  "type": "string"
}
```
- **Title**: A title for display and navigation
```json
{
  "title": "Title",
  "description": "A title for display and navigation",
  "$id": "#/definitions/title",
  "type": "string"
}
```
- **URL**: URL for web site or Internet presence
```json
{
  "title": "URL",
  "description": "URL for web site or Internet presence",
  "$id": "#/definitions/url",
  "type": "string",
  "format": "uri"
}
```
- **Document version**: The version of the document content.
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

- **Addition**: Specifies contents to be added into controls, in resolution
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
      "anyOf": [
        {
          "$ref": "#/definitions/param"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/param"
          },
          "minItems": 2
        }
      ]
    },
    "properties": {
      "anyOf": [
        {
          "$ref": "#/definitions/prop"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/prop"
          },
          "minItems": 2
        }
      ]
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
      "anyOf": [
        {
          "$ref": "#/definitions/link"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/link"
          },
          "minItems": 2
        }
      ]
    },
    "parts": {
      "anyOf": [
        {
          "$ref": "#/definitions/part"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/part"
          },
          "minItems": 2
        }
      ]
    }
  },
  "additionalProperties": false
}
```
- **Address line**: A single line of an address.
```json
{
  "title": "Address line",
  "description": "A single line of an address.",
  "$id": "#/definitions/addr-line",
  "type": "string"
}
```
- **Address**: A postal address.
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
      "anyOf": [
        {
          "$ref": "#/definitions/addr-line"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/addr-line"
          },
          "minItems": 2
        }
      ]
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
- **Include all**: Include all controls from the imported resource (catalog)
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
- **Alteration**: An Alter element specifies changes to be made to an included control when a profile is resolved.
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
      "anyOf": [
        {
          "$ref": "#/definitions/remove"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/remove"
          },
          "minItems": 2
        }
      ]
    },
    "additions": {
      "anyOf": [
        {
          "$ref": "#/definitions/add"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/add"
          },
          "minItems": 2
        }
      ]
    }
  },
  "additionalProperties": false
}
```
- **Annotation**: A name/value pair with optional explanatory remarks.
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
- **As is**: An As-is element indicates that the controls should be structured in resolution as they are structured in their source catalogs. It does not contain any elements or attributes.
```json
{
  "title": "As is",
  "description": "An As-is element indicates that the controls should be structured in resolution as they are structured in their source catalogs. It does not contain any elements or attributes.",
  "$id": "#/definitions/as-is",
  "type": "boolean"
}
```
- **Back matter**: A collection of citations and resource references.
```json
{
  "title": "Back matter",
  "description": "A collection of citations and resource references.",
  "$id": "#/definitions/back-matter",
  "type": "object",
  "properties": {
    "citations": {
      "anyOf": [
        {
          "$ref": "#/definitions/citation"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/citation"
          },
          "minItems": 2
        }
      ]
    },
    "resources": {
      "anyOf": [
        {
          "$ref": "#/definitions/resource"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/resource"
          },
          "minItems": 2
        }
      ]
    }
  },
  "additionalProperties": false
}
```
- **Base64**: 
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
- **Call**: Call a control by its ID
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
- **Choice**: A value selection among several such options
```json
{
  "title": "Choice",
  "description": "A value selection among several such options",
  "$id": "#/definitions/choice",
  "type": "string"
}
```
- **Citation**: A citation to resources, either external or internal (by means of internal cross-reference).
```json
{
  "title": "Citation",
  "description": "A citation to resources, either external or internal (by means of internal cross-reference).",
  "$id": "#/definitions/citation",
  "type": "object",
  "properties": {
    "id": {
      "title": "Identifier",
      "description": "Unique identifier of the containing object",
      "type": "string"
    },
    "targets": {
      "anyOf": [
        {
          "$ref": "#/definitions/target"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/target"
          },
          "minItems": 2
        }
      ]
    },
    "title": {
      "$ref": "#/definitions/title"
    },
    "desc": {
      "$ref": "#/definitions/desc"
    },
    "document-ids": {
      "anyOf": [
        {
          "$ref": "#/definitions/doc-id"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/doc-id"
          },
          "minItems": 2
        }
      ]
    },
    "properties": {
      "anyOf": [
        {
          "$ref": "#/definitions/prop"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/prop"
          },
          "minItems": 2
        }
      ]
    }
  },
  "required": [
    "id"
  ],
  "additionalProperties": false
}
```
- **City**: City, town or geographical region for mailing address
```json
{
  "title": "City",
  "description": "City, town or geographical region for mailing address",
  "$id": "#/definitions/city",
  "type": "string"
}
```
- **Combination rule**: A Combine element defines whether and how to combine multiple (competing) versions of the same control
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
- **Constraint**: A formal or informal expression of a constraint or test
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
- **Country**: Country for mailing address
```json
{
  "title": "Country",
  "description": "Country for mailing address",
  "$id": "#/definitions/country",
  "type": "string"
}
```
- **Custom grouping**: A Custom element frames a structure for embedding represented controls in resolution.
```json
{
  "title": "Custom grouping",
  "description": "A Custom element frames a structure for embedding represented controls in resolution.",
  "$id": "#/definitions/custom",
  "type": "object",
  "properties": {
    "groups": {
      "anyOf": [
        {
          "$ref": "#/definitions/group"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/group"
          },
          "minItems": 2
        }
      ]
    },
    "id-selectors": {
      "anyOf": [
        {
          "$ref": "#/definitions/call"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/call"
          },
          "minItems": 2
        }
      ]
    },
    "pattern-selectors": {
      "anyOf": [
        {
          "$ref": "#/definitions/match"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/match"
          },
          "minItems": 2
        }
      ]
    }
  },
  "additionalProperties": false
}
```
- **Description**: A short textual description
```json
{
  "title": "Description",
  "description": "A short textual description",
  "$id": "#/definitions/desc",
  "type": "string"
}
```
- **Document Identifier**: A document identifier qualified by an identifier type.
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
- **Email**: Email address
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
- **Exclude controls**: Which controls to exclude from the resource (source catalog) being imported
```json
{
  "title": "Exclude controls",
  "description": "Which controls to exclude from the resource (source catalog) being imported",
  "$id": "#/definitions/exclude",
  "type": "object",
  "properties": {
    "id-selectors": {
      "anyOf": [
        {
          "$ref": "#/definitions/call"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/call"
          },
          "minItems": 2
        }
      ]
    },
    "pattern-selectors": {
      "anyOf": [
        {
          "$ref": "#/definitions/match"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/match"
          },
          "minItems": 2
        }
      ]
    }
  },
  "additionalProperties": false
}
```
- **Control group**: As in catalogs, a group of (selected) controls or of groups of controls
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
      "anyOf": [
        {
          "$ref": "#/definitions/param"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/param"
          },
          "minItems": 2
        }
      ]
    },
    "properties": {
      "anyOf": [
        {
          "$ref": "#/definitions/prop"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/prop"
          },
          "minItems": 2
        }
      ]
    },
    "parts": {
      "anyOf": [
        {
          "$ref": "#/definitions/part"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/part"
          },
          "minItems": 2
        }
      ]
    },
    "groups": {
      "anyOf": [
        {
          "$ref": "#/definitions/group"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/group"
          },
          "minItems": 2
        }
      ]
    },
    "id-selectors": {
      "anyOf": [
        {
          "$ref": "#/definitions/call"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/call"
          },
          "minItems": 2
        }
      ]
    },
    "pattern-selectors": {
      "anyOf": [
        {
          "$ref": "#/definitions/match"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/match"
          },
          "minItems": 2
        }
      ]
    }
  },
  "additionalProperties": false
}
```
- **Guideline**: A prose statement that provides a recommendation for the use of a parameter.
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
- **Hash**: A representation of a cryptographic digest generated over a resource using a hash algorithm.
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
- **Import resource**: An Import element designates a catalog, profile, or other resource to be included (referenced and potentially modified) by this profile.
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
- **Include controls**: Specifies which controls to include from the resource (source catalog) being imported
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
      "anyOf": [
        {
          "$ref": "#/definitions/call"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/call"
          },
          "minItems": 2
        }
      ]
    },
    "pattern-selectors": {
      "anyOf": [
        {
          "$ref": "#/definitions/match"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/match"
          },
          "minItems": 2
        }
      ]
    }
  },
  "additionalProperties": false
}
```
- **Parameter label**: A placeholder for a missing value, in display.
```json
{
  "title": "Parameter label",
  "description": "A placeholder for a missing value, in display.",
  "$id": "#/definitions/label",
  "type": "string"
}
```
- **Last modified timestamp**: Date and time of last modification.
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
- **Link**: A reference to a local or remote resource
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
- **Match controls by identifier**: Select controls by (regular expression) match on ID
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
- **Merge controls**: A Merge element merges controls in resolution.
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
- **Publication metadata**: Provides information about the publication and availability of the containing document.
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
    "document-ids": {
      "anyOf": [
        {
          "$ref": "#/definitions/doc-id"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/doc-id"
          },
          "minItems": 2
        }
      ]
    },
    "properties": {
      "anyOf": [
        {
          "$ref": "#/definitions/prop"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/prop"
          },
          "minItems": 2
        }
      ]
    },
    "links": {
      "anyOf": [
        {
          "$ref": "#/definitions/link"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/link"
          },
          "minItems": 2
        }
      ]
    },
    "roles": {
      "anyOf": [
        {
          "$ref": "#/definitions/role"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/role"
          },
          "minItems": 2
        }
      ]
    },
    "parties": {
      "anyOf": [
        {
          "$ref": "#/definitions/party"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/party"
          },
          "minItems": 2
        }
      ]
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
- **Modify controls**: Set parameters or amend controls in resolution
```json
{
  "title": "Modify controls",
  "description": "Set parameters or amend controls in resolution",
  "$id": "#/definitions/modify",
  "type": "object",
  "properties": {
    "settings": {
      "type": "object",
      "minProperties": 1,
      "additionalProperties": {
        "allOf": [
          {
            "type": "object",
            "$ref": "#/definitions/set"
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
      "anyOf": [
        {
          "$ref": "#/definitions/alter"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/alter"
          },
          "minItems": 2
        }
      ]
    }
  },
  "additionalProperties": false
}
```
- **Organization**: An organization or legal entity (not a person), with contact information
```json
{
  "title": "Organization",
  "description": "An organization or legal entity (not a person), with contact information",
  "$id": "#/definitions/org",
  "type": "object",
  "properties": {
    "org-name": {
      "$ref": "#/definitions/org-name"
    },
    "short-name": {
      "$ref": "#/definitions/short-name"
    },
    "organization-ids": {
      "anyOf": [
        {
          "$ref": "#/definitions/org-id"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/org-id"
          },
          "minItems": 2
        }
      ]
    },
    "addresses": {
      "anyOf": [
        {
          "$ref": "#/definitions/address"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/address"
          },
          "minItems": 2
        }
      ]
    },
    "email-addresses": {
      "anyOf": [
        {
          "$ref": "#/definitions/email"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/email"
          },
          "minItems": 2
        }
      ]
    },
    "telephone-numbers": {
      "anyOf": [
        {
          "$ref": "#/definitions/phone"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/phone"
          },
          "minItems": 2
        }
      ]
    },
    "URLs": {
      "anyOf": [
        {
          "$ref": "#/definitions/url"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/url"
          },
          "minItems": 2
        }
      ]
    },
    "properties": {
      "anyOf": [
        {
          "$ref": "#/definitions/prop"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/prop"
          },
          "minItems": 2
        }
      ]
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
      "anyOf": [
        {
          "$ref": "#/definitions/link"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/link"
          },
          "minItems": 2
        }
      ]
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "org-name"
  ],
  "additionalProperties": false
}
```
- **Organization Identifier**: An identifier for an organization using a designated scheme.
```json
{
  "title": "Organization Identifier",
  "description": "An identifier for an organization using a designated scheme.",
  "$id": "#/definitions/org-id",
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
    "id"
  ],
  "additionalProperties": false
}
```
- **Organization Name**: Full (legal) name of an organization
```json
{
  "title": "Organization Name",
  "description": "Full (legal) name of an organization",
  "$id": "#/definitions/org-name",
  "type": "string"
}
```
- **OSCAL version**: OSCAL model version.
```json
{
  "title": "OSCAL version",
  "description": "OSCAL model version.",
  "$id": "#/definitions/oscal-version",
  "type": "string"
}
```
- **Parameter**: Parameters provide a mechanism for the dynamic assignment of value(s) in a control.
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
      "anyOf": [
        {
          "$ref": "#/definitions/usage"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/usage"
          },
          "minItems": 2
        }
      ]
    },
    "constraints": {
      "anyOf": [
        {
          "$ref": "#/definitions/constraint"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/constraint"
          },
          "minItems": 2
        }
      ]
    },
    "guidance": {
      "anyOf": [
        {
          "$ref": "#/definitions/guideline"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/guideline"
          },
          "minItems": 2
        }
      ]
    },
    "value": {
      "$ref": "#/definitions/value"
    },
    "select": {
      "$ref": "#/definitions/select"
    },
    "links": {
      "anyOf": [
        {
          "$ref": "#/definitions/link"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/link"
          },
          "minItems": 2
        }
      ]
    }
  },
  "required": [
    "id"
  ],
  "additionalProperties": false
}
```
- **Part**: A partition or component of a control or part
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
      "anyOf": [
        {
          "$ref": "#/definitions/prop"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/prop"
          },
          "minItems": 2
        }
      ]
    },
    "prose": {
      "$ref": "#/definitions/prose"
    },
    "parts": {
      "anyOf": [
        {
          "$ref": "#/definitions/part"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/part"
          },
          "minItems": 2
        }
      ]
    },
    "links": {
      "anyOf": [
        {
          "$ref": "#/definitions/link"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/link"
          },
          "minItems": 2
        }
      ]
    }
  },
  "required": [
    "name"
  ],
  "additionalProperties": false
}
```
- **Party (organization or person)**: A responsible entity, either singular (an organization or person) or collective (multiple persons)
```json
{
  "title": "Party (organization or person)",
  "description": "A responsible entity, either singular (an organization or person) or collective (multiple persons)",
  "$id": "#/definitions/party",
  "type": "object",
  "properties": {
    "id": {
      "title": "Identifier",
      "description": "Unique identifier of the containing object",
      "type": "string"
    },
    "persons": {
      "anyOf": [
        {
          "$ref": "#/definitions/person"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/person"
          },
          "minItems": 2
        }
      ]
    },
    "org": {
      "$ref": "#/definitions/org"
    },
    "properties": {
      "anyOf": [
        {
          "$ref": "#/definitions/prop"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/prop"
          },
          "minItems": 2
        }
      ]
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
      "anyOf": [
        {
          "$ref": "#/definitions/link"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/link"
          },
          "minItems": 2
        }
      ]
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "additionalProperties": false
}
```
- **Party Reference**: References a party defined in metadata.
```json
{
  "title": "Party Reference",
  "description": "References a party defined in metadata.",
  "$id": "#/definitions/party-id",
  "type": "string"
}
```
- **Person**: A person, with contact information
```json
{
  "title": "Person",
  "description": "A person, with contact information",
  "$id": "#/definitions/person",
  "type": "object",
  "properties": {
    "person-name": {
      "$ref": "#/definitions/person-name"
    },
    "short-name": {
      "$ref": "#/definitions/short-name"
    },
    "org-name": {
      "$ref": "#/definitions/org-name"
    },
    "person-ids": {
      "anyOf": [
        {
          "$ref": "#/definitions/person-id"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/person-id"
          },
          "minItems": 2
        }
      ]
    },
    "organization-ids": {
      "anyOf": [
        {
          "$ref": "#/definitions/org-id"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/org-id"
          },
          "minItems": 2
        }
      ]
    },
    "addresses": {
      "anyOf": [
        {
          "$ref": "#/definitions/address"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/address"
          },
          "minItems": 2
        }
      ]
    },
    "email-addresses": {
      "anyOf": [
        {
          "$ref": "#/definitions/email"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/email"
          },
          "minItems": 2
        }
      ]
    },
    "telephone-numbers": {
      "anyOf": [
        {
          "$ref": "#/definitions/phone"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/phone"
          },
          "minItems": 2
        }
      ]
    },
    "URLs": {
      "anyOf": [
        {
          "$ref": "#/definitions/url"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/url"
          },
          "minItems": 2
        }
      ]
    },
    "properties": {
      "anyOf": [
        {
          "$ref": "#/definitions/prop"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/prop"
          },
          "minItems": 2
        }
      ]
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
      "anyOf": [
        {
          "$ref": "#/definitions/link"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/link"
          },
          "minItems": 2
        }
      ]
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "additionalProperties": false
}
```
- **Personal Identifier**: An identifier for a person (such as an ORCID) using a designated scheme.
```json
{
  "title": "Personal Identifier",
  "description": "An identifier for a person (such as an ORCID) using a designated scheme.",
  "$id": "#/definitions/person-id",
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
    "id"
  ],
  "additionalProperties": false
}
```
- **Person Name**: Full (legal) name of an individual
```json
{
  "title": "Person Name",
  "description": "Full (legal) name of an individual",
  "$id": "#/definitions/person-name",
  "type": "string"
}
```
- **Telephone**: Contact number by telephone
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
- **Postal Code**: Postal or ZIP code for mailing address
```json
{
  "title": "Postal Code",
  "description": "Postal or ZIP code for mailing address",
  "$id": "#/definitions/postal-code",
  "type": "string"
}
```
- **Profile**: Each OSCAL profile is defined by a Profile element
```json
{
  "title": "Profile",
  "description": "Each OSCAL profile is defined by a Profile element",
  "$id": "#/definitions/profile",
  "type": "object",
  "properties": {
    "id": {
      "title": "Identifier",
      "description": "Unique identifier of the containing object",
      "type": "string"
    },
    "metadata": {
      "$ref": "#/definitions/metadata"
    },
    "imports": {
      "anyOf": [
        {
          "$ref": "#/definitions/import"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/import"
          },
          "minItems": 2
        }
      ]
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
    "id",
    "metadata"
  ],
  "additionalProperties": false
}
```
- **Property**: A value with a name, attributed to the containing control, part, or group.
```json
{
  "title": "Property",
  "description": "A value with a name, attributed to the containing control, part, or group.",
  "$id": "#/definitions/prop",
  "type": "object",
  "properties": {
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
    }
  },
  "minProperties": 1,
  "maxProperties": 4
}
```
- **Prose**: Prose permits multiple paragraphs, lists, tables etc.
```json
{
  "title": "Prose",
  "description": "Prose permits multiple paragraphs, lists, tables etc.",
  "$id": "#/definitions/prose",
  "type": "string"
}
```
- **Publication Timestamp**: The date and time this document was published.
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
- **Remarks**: Additional commentary on the parent item.
```json
{
  "title": "Remarks",
  "description": "Additional commentary on the parent item.",
  "$id": "#/definitions/remarks",
  "type": "string"
}
```
- **Removal**: Specifies elements to be removed from a control, in resolution
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
- **Resource**: A resource associated with the present document.
```json
{
  "title": "Resource",
  "description": "A resource associated with the present document.",
  "$id": "#/definitions/resource",
  "type": "object",
  "properties": {
    "id": {
      "title": "Identifier",
      "description": "Unique identifier of the containing object",
      "type": "string"
    },
    "desc": {
      "$ref": "#/definitions/desc"
    },
    "properties": {
      "anyOf": [
        {
          "$ref": "#/definitions/prop"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/prop"
          },
          "minItems": 2
        }
      ]
    },
    "rlinks": {
      "anyOf": [
        {
          "$ref": "#/definitions/rlink"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/rlink"
          },
          "minItems": 2
        }
      ]
    },
    "base64": {
      "$ref": "#/definitions/base64"
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "id"
  ],
  "additionalProperties": false
}
```
- **Responsible Party**: A reference to a set of organizations or persons that have responsibility for performing a referenced role relative to the parent context.
```json
{
  "title": "Responsible Party",
  "description": "A reference to a set of organizations or persons that have responsibility for performing a referenced role relative to the parent context.",
  "$id": "#/definitions/responsible-party",
  "type": "object",
  "properties": {
    "party-ids": {
      "anyOf": [
        {
          "$ref": "#/definitions/party-id"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/party-id"
          },
          "minItems": 2
        }
      ]
    },
    "properties": {
      "anyOf": [
        {
          "$ref": "#/definitions/prop"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/prop"
          },
          "minItems": 2
        }
      ]
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
      "anyOf": [
        {
          "$ref": "#/definitions/link"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/link"
          },
          "minItems": 2
        }
      ]
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "party-ids"
  ],
  "additionalProperties": false
}
```
- **Resource link**: A pointer to an external copy of a document with optional hash for verification
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
      "anyOf": [
        {
          "$ref": "#/definitions/hash"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/hash"
          },
          "minItems": 2
        }
      ]
    }
  },
  "required": [
    "href"
  ],
  "additionalProperties": false
}
```
- **Role**: Defining a role to be assigned to a party
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
      "anyOf": [
        {
          "$ref": "#/definitions/prop"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/prop"
          },
          "minItems": 2
        }
      ]
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
      "anyOf": [
        {
          "$ref": "#/definitions/link"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/link"
          },
          "minItems": 2
        }
      ]
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
- **Selection**: Presenting a choice among alternatives
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
      "anyOf": [
        {
          "$ref": "#/definitions/choice"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/choice"
          },
          "minItems": 2
        }
      ]
    }
  },
  "additionalProperties": false
}
```
- **Parameter Setting**: A parameter setting, to be propagated to points of insertion
```json
{
  "title": "Parameter Setting",
  "description": "A parameter setting, to be propagated to points of insertion",
  "$id": "#/definitions/set",
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
      "anyOf": [
        {
          "$ref": "#/definitions/usage"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/usage"
          },
          "minItems": 2
        }
      ]
    },
    "constraints": {
      "anyOf": [
        {
          "$ref": "#/definitions/constraint"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/constraint"
          },
          "minItems": 2
        }
      ]
    },
    "guidance": {
      "anyOf": [
        {
          "$ref": "#/definitions/guideline"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/guideline"
          },
          "minItems": 2
        }
      ]
    },
    "value": {
      "$ref": "#/definitions/value"
    },
    "select": {
      "$ref": "#/definitions/select"
    },
    "links": {
      "anyOf": [
        {
          "$ref": "#/definitions/link"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/link"
          },
          "minItems": 2
        }
      ]
    }
  },
  "additionalProperties": false
}
```
- **short-name**: A common name, short name or acronym
```json
{
  "title": "short-name",
  "description": "A common name, short name or acronym",
  "$id": "#/definitions/short-name",
  "type": "string"
}
```
- **State**: State, province or analogous geographical region for mailing address
```json
{
  "title": "State",
  "description": "State, province or analogous geographical region for mailing address",
  "$id": "#/definitions/state",
  "type": "string"
}
```
- **Citation target**: An address for retrieval of a citation
```json
{
  "title": "Citation target",
  "description": "An address for retrieval of a citation",
  "$id": "#/definitions/target",
  "type": "string"
}
```
- **Title**: A title for display and navigation
```json
{
  "title": "Title",
  "description": "A title for display and navigation",
  "$id": "#/definitions/title",
  "type": "string"
}
```
- **URL**: URL for web site or Internet presence
```json
{
  "title": "URL",
  "description": "URL for web site or Internet presence",
  "$id": "#/definitions/url",
  "type": "string",
  "format": "uri"
}
```
- **Parameter description**: Indicates and explains the purpose and use of a parameter
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
- **Value constraint**: Indicates a permissible value for a parameter or property
```json
{
  "title": "Value constraint",
  "description": "Indicates a permissible value for a parameter or property",
  "$id": "#/definitions/value",
  "type": "string"
}
```
- **Document version**: The version of the document content.
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

- **Address line**: A single line of an address.
```json
{
  "title": "Address line",
  "description": "A single line of an address.",
  "$id": "#/definitions/addr-line",
  "type": "string"
}
```
- **Address**: A postal address.
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
      "anyOf": [
        {
          "$ref": "#/definitions/addr-line"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/addr-line"
          },
          "minItems": 2
        }
      ]
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
- **Adjustment Justification**: If the selected security level is different from the base security level, this contains the justification for the change.
```json
{
  "title": "Adjustment Justification",
  "description": "If the selected security level is different from the base security level, this contains the justification for the change.",
  "$id": "#/definitions/adjustment-justification",
  "type": "string"
}
```
- **Annotation**: A name/value pair with optional explanatory remarks.
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
- **Authorization Boundary**: A description of this system's authorization boundary, optionally supplemented by diagrams that illustrate the authorization boundary.
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
      "anyOf": [
        {
          "$ref": "#/definitions/prop"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/prop"
          },
          "minItems": 2
        }
      ]
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
      "anyOf": [
        {
          "$ref": "#/definitions/link"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/link"
          },
          "minItems": 2
        }
      ]
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
- **Privilege**: Identifies a specific system privilege held by the user, along with an associated description and/or rationale for the privilege.
```json
{
  "title": "Privilege",
  "description": "Identifies a specific system privilege held by the user, along with an associated description and/or rationale for the privilege.",
  "$id": "#/definitions/authorized-privilege",
  "type": "object",
  "properties": {
    "name": {
      "title": "Privilege Name",
      "description": "The name of the identified privilege.",
      "type": "string"
    },
    "description": {
      "$ref": "#/definitions/description"
    },
    "functions-performed": {
      "anyOf": [
        {
          "$ref": "#/definitions/function-performed"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/function-performed"
          },
          "minItems": 2
        }
      ]
    }
  },
  "required": [
    "name",
    "functions-performed"
  ],
  "additionalProperties": false
}
```
- **Availability Impact Level**: The expected level of impact resulting from the disruption of access to or use of information or the information system.
```json
{
  "title": "Availability Impact Level",
  "description": "The expected level of impact resulting from the disruption of access to or use of information or the information system.",
  "$id": "#/definitions/availability-impact",
  "type": "object",
  "properties": {
    "properties": {
      "anyOf": [
        {
          "$ref": "#/definitions/prop"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/prop"
          },
          "minItems": 2
        }
      ]
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
- **Back matter**: A collection of citations and resource references.
```json
{
  "title": "Back matter",
  "description": "A collection of citations and resource references.",
  "$id": "#/definitions/back-matter",
  "type": "object",
  "properties": {
    "citations": {
      "anyOf": [
        {
          "$ref": "#/definitions/citation"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/citation"
          },
          "minItems": 2
        }
      ]
    },
    "resources": {
      "anyOf": [
        {
          "$ref": "#/definitions/resource"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/resource"
          },
          "minItems": 2
        }
      ]
    }
  },
  "additionalProperties": false
}
```
- **Base Level (Confidentiality, Integrity, or Availability)**: The prescribed base (Confidentiality, Integrity, or Availability) security impact level.
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
- **Base64**: 
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
- **Component Control Implementation**: Defines how the referenced component implements a set of controls.
```json
{
  "title": "Component Control Implementation",
  "description": "Defines how the referenced component implements a set of controls.",
  "$id": "#/definitions/by-component",
  "type": "object",
  "properties": {
    "description": {
      "$ref": "#/definitions/description"
    },
    "properties": {
      "anyOf": [
        {
          "$ref": "#/definitions/prop"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/prop"
          },
          "minItems": 2
        }
      ]
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
      "anyOf": [
        {
          "$ref": "#/definitions/link"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/link"
          },
          "minItems": 2
        }
      ]
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
    "set-params": {
      "type": "object",
      "minProperties": 1,
      "additionalProperties": {
        "allOf": [
          {
            "type": "object",
            "$ref": "#/definitions/set-param"
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
    "description"
  ],
  "additionalProperties": false
}
```
- **Caption**: A brief caption to annotate the diagram.
```json
{
  "title": "Caption",
  "description": "A brief caption to annotate the diagram.",
  "$id": "#/definitions/caption",
  "type": "string"
}
```
- **Citation**: A citation to resources, either external or internal (by means of internal cross-reference).
```json
{
  "title": "Citation",
  "description": "A citation to resources, either external or internal (by means of internal cross-reference).",
  "$id": "#/definitions/citation",
  "type": "object",
  "properties": {
    "id": {
      "title": "Identifier",
      "description": "Unique identifier of the containing object",
      "type": "string"
    },
    "targets": {
      "anyOf": [
        {
          "$ref": "#/definitions/target"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/target"
          },
          "minItems": 2
        }
      ]
    },
    "title": {
      "$ref": "#/definitions/title"
    },
    "desc": {
      "$ref": "#/definitions/desc"
    },
    "document-ids": {
      "anyOf": [
        {
          "$ref": "#/definitions/doc-id"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/doc-id"
          },
          "minItems": 2
        }
      ]
    },
    "properties": {
      "anyOf": [
        {
          "$ref": "#/definitions/prop"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/prop"
          },
          "minItems": 2
        }
      ]
    }
  },
  "required": [
    "id"
  ],
  "additionalProperties": false
}
```
- **City**: City, town or geographical region for mailing address
```json
{
  "title": "City",
  "description": "City, town or geographical region for mailing address",
  "$id": "#/definitions/city",
  "type": "string"
}
```
- **Component**: A defined component that can be part of an implemented system.
```json
{
  "title": "Component",
  "description": "A defined component that can be part of an implemented system.",
  "$id": "#/definitions/component",
  "type": "object",
  "properties": {
    "name": {
      "title": "Component Name",
      "description": "The component's human-readable name.",
      "type": "string"
    },
    "component-type": {
      "title": "Component Type",
      "description": "A category describing the purpose of the component.",
      "type": "string"
    },
    "description": {
      "$ref": "#/definitions/description"
    },
    "properties": {
      "anyOf": [
        {
          "$ref": "#/definitions/prop"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/prop"
          },
          "minItems": 2
        }
      ]
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
      "anyOf": [
        {
          "$ref": "#/definitions/link"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/link"
          },
          "minItems": 2
        }
      ]
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
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "name",
    "component-type",
    "description",
    "status"
  ],
  "additionalProperties": false
}
```
- **Confidentiality Impact Level**: The expected level of impact resulting from the unauthorized disclosure of information.
```json
{
  "title": "Confidentiality Impact Level",
  "description": "The expected level of impact resulting from the unauthorized disclosure of information.",
  "$id": "#/definitions/confidentiality-impact",
  "type": "object",
  "properties": {
    "properties": {
      "anyOf": [
        {
          "$ref": "#/definitions/prop"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/prop"
          },
          "minItems": 2
        }
      ]
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
- **Control Implementation**: Describes how the system satisfies a set of controls.
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
      "anyOf": [
        {
          "$ref": "#/definitions/implemented-requirement"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/implemented-requirement"
          },
          "minItems": 2
        }
      ]
    }
  },
  "required": [
    "description",
    "implemented-requirements"
  ],
  "additionalProperties": false
}
```
- **Country**: Country for mailing address
```json
{
  "title": "Country",
  "description": "Country for mailing address",
  "$id": "#/definitions/country",
  "type": "string"
}
```
- **Data Flow**: A description of the logical flow of information within the system and across its boundaries, optionally supplemented by diagrams that illustrate these flows.
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
      "anyOf": [
        {
          "$ref": "#/definitions/prop"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/prop"
          },
          "minItems": 2
        }
      ]
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
      "anyOf": [
        {
          "$ref": "#/definitions/link"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/link"
          },
          "minItems": 2
        }
      ]
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
- **System Authorization Date**: The date this system received its authorization.
```json
{
  "title": "System Authorization Date",
  "description": "The date this system received its authorization.",
  "$id": "#/definitions/date-authorized",
  "type": "string",
  "pattern": "^((2000|2400|2800|(19|2[0-9](0[48]|[2468][048]|[13579][26])))-02-29)|(((19|2[0-9])[0-9]{2})-02-(0[1-9]|1[0-9]|2[0-8]))|(((19|2[0-9])[0-9]{2})-(0[13578]|10|12)-(0[1-9]|[12][0-9]|3[01]))|(((19|2[0-9])[0-9]{2})-(0[469]|11)-(0[1-9]|[12][0-9]|30))(Z|[+-][0-9]{2}:[0-9]{2})?$"
}
```
- **Description**: A short textual description
```json
{
  "title": "Description",
  "description": "A short textual description",
  "$id": "#/definitions/desc",
  "type": "string"
}
```
- **Description**: A description supporting the parent item.
```json
{
  "title": "Description",
  "description": "A description supporting the parent item.",
  "$id": "#/definitions/description",
  "type": "string"
}
```
- **Diagram**: A graphic that provides a visual representation the system, or some aspect of it.
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
      "anyOf": [
        {
          "$ref": "#/definitions/prop"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/prop"
          },
          "minItems": 2
        }
      ]
    },
    "links": {
      "anyOf": [
        {
          "$ref": "#/definitions/link"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/link"
          },
          "minItems": 2
        }
      ]
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
- **Document Identifier**: A document identifier qualified by an identifier type.
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
- **Email**: Email address
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
- **Functions Performed**: Describes a function performed for a given authorized privilege by this user class.
```json
{
  "title": "Functions Performed",
  "description": "Describes a function performed for a given authorized privilege by this user class.",
  "$id": "#/definitions/function-performed",
  "type": "string"
}
```
- **Hash**: A representation of a cryptographic digest generated over a resource using a hash algorithm.
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
- **Implemented Component**: The set of componenets that are implemented in a given system inventory item.
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
      "anyOf": [
        {
          "$ref": "#/definitions/prop"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/prop"
          },
          "minItems": 2
        }
      ]
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
      "anyOf": [
        {
          "$ref": "#/definitions/link"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/link"
          },
          "minItems": 2
        }
      ]
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
- **Control-based Requirement**: Describes how the system satisfies an individual control.
```json
{
  "title": "Control-based Requirement",
  "description": "Describes how the system satisfies an individual control.",
  "$id": "#/definitions/implemented-requirement",
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
      "anyOf": [
        {
          "$ref": "#/definitions/prop"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/prop"
          },
          "minItems": 2
        }
      ]
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
      "anyOf": [
        {
          "$ref": "#/definitions/link"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/link"
          },
          "minItems": 2
        }
      ]
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
    "set-params": {
      "type": "object",
      "minProperties": 1,
      "additionalProperties": {
        "allOf": [
          {
            "type": "object",
            "$ref": "#/definitions/set-param"
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
    "control-id"
  ],
  "additionalProperties": false
}
```
- **Import Profile**: Used to import the OSCAL profile representing the system's control baseline.
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
- **Information Type**: Contains details about one information type that is stored, processed, or transmitted by the system, such as privacy information, and those defined in NIST SP 800-60.
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
    "name": {
      "title": "Information Type Name",
      "description": "The name of the information type.",
      "type": "string"
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
      "anyOf": [
        {
          "$ref": "#/definitions/prop"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/prop"
          },
          "minItems": 2
        }
      ]
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
    "name",
    "description",
    "confidentiality-impact",
    "integrity-impact",
    "availability-impact"
  ],
  "additionalProperties": false
}
```
- **Information Type Identifier**: An identifier qualified by the given identification system used, such as NIST SP 800-60.
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
- **Integrity Impact Level**: The expected level of impact resulting from the unauthorized modification of information.
```json
{
  "title": "Integrity Impact Level",
  "description": "The expected level of impact resulting from the unauthorized modification of information.",
  "$id": "#/definitions/integrity-impact",
  "type": "object",
  "properties": {
    "properties": {
      "anyOf": [
        {
          "$ref": "#/definitions/prop"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/prop"
          },
          "minItems": 2
        }
      ]
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
- **Interconnection**: Details on an individual system interconnection.
```json
{
  "title": "Interconnection",
  "description": "Details on an individual system interconnection.",
  "$id": "#/definitions/interconnection",
  "type": "object",
  "properties": {
    "id": {
      "title": "Identifier",
      "description": "Unique identifier of the containing object",
      "type": "string"
    },
    "remote-system-name": {
      "$ref": "#/definitions/remote-system-name"
    },
    "properties": {
      "anyOf": [
        {
          "$ref": "#/definitions/prop"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/prop"
          },
          "minItems": 2
        }
      ]
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
      "anyOf": [
        {
          "$ref": "#/definitions/link"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/link"
          },
          "minItems": 2
        }
      ]
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
- **Inventory Item**: A single managed inventory item within the system.
```json
{
  "title": "Inventory Item",
  "description": "A single managed inventory item within the system.",
  "$id": "#/definitions/inventory-item",
  "type": "object",
  "properties": {
    "id": {
      "title": "Identifier",
      "description": "Unique identifier of the containing object",
      "type": "string"
    },
    "asset-id": {
      "title": "Asset Identifier",
      "description": "Organizational asset identifier that is unique in the context of the system. This may be a reference to the identifier used in an asset tracking system or a vulnerability scanning tool.",
      "type": "string"
    },
    "description": {
      "$ref": "#/definitions/description"
    },
    "properties": {
      "anyOf": [
        {
          "$ref": "#/definitions/prop"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/prop"
          },
          "minItems": 2
        }
      ]
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
      "anyOf": [
        {
          "$ref": "#/definitions/link"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/link"
          },
          "minItems": 2
        }
      ]
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
    "id",
    "asset-id",
    "description"
  ],
  "additionalProperties": false
}
```
- **Last modified timestamp**: Date and time of last modification.
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
- **Leveraged Authorization**: A description of another authorized system from which this system inherits capabilities that satisfy security requirements. Another term for this concept is a common control provider.
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
    "name": {
      "title": "Name",
      "description": "Identifying the purpose and intended use of the property, part or other object.",
      "type": "string"
    },
    "properties": {
      "anyOf": [
        {
          "$ref": "#/definitions/prop"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/prop"
          },
          "minItems": 2
        }
      ]
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
      "anyOf": [
        {
          "$ref": "#/definitions/link"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/link"
          },
          "minItems": 2
        }
      ]
    },
    "party-id": {
      "$ref": "#/definitions/party-id"
    },
    "date-authorized": {
      "$ref": "#/definitions/date-authorized"
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "name",
    "party-id",
    "date-authorized"
  ],
  "additionalProperties": false
}
```
- **Link**: A reference to a local or remote resource
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
- **Publication metadata**: Provides information about the publication and availability of the containing document.
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
    "document-ids": {
      "anyOf": [
        {
          "$ref": "#/definitions/doc-id"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/doc-id"
          },
          "minItems": 2
        }
      ]
    },
    "properties": {
      "anyOf": [
        {
          "$ref": "#/definitions/prop"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/prop"
          },
          "minItems": 2
        }
      ]
    },
    "links": {
      "anyOf": [
        {
          "$ref": "#/definitions/link"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/link"
          },
          "minItems": 2
        }
      ]
    },
    "roles": {
      "anyOf": [
        {
          "$ref": "#/definitions/role"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/role"
          },
          "minItems": 2
        }
      ]
    },
    "parties": {
      "anyOf": [
        {
          "$ref": "#/definitions/party"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/party"
          },
          "minItems": 2
        }
      ]
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
- **Network Architecture**: A description of the system's network architecture, optionally supplemented by diagrams that illustrate the network architecture.
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
      "anyOf": [
        {
          "$ref": "#/definitions/prop"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/prop"
          },
          "minItems": 2
        }
      ]
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
      "anyOf": [
        {
          "$ref": "#/definitions/link"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/link"
          },
          "minItems": 2
        }
      ]
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
- **Organization**: An organization or legal entity (not a person), with contact information
```json
{
  "title": "Organization",
  "description": "An organization or legal entity (not a person), with contact information",
  "$id": "#/definitions/org",
  "type": "object",
  "properties": {
    "org-name": {
      "$ref": "#/definitions/org-name"
    },
    "short-name": {
      "$ref": "#/definitions/short-name"
    },
    "organization-ids": {
      "anyOf": [
        {
          "$ref": "#/definitions/org-id"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/org-id"
          },
          "minItems": 2
        }
      ]
    },
    "addresses": {
      "anyOf": [
        {
          "$ref": "#/definitions/address"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/address"
          },
          "minItems": 2
        }
      ]
    },
    "email-addresses": {
      "anyOf": [
        {
          "$ref": "#/definitions/email"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/email"
          },
          "minItems": 2
        }
      ]
    },
    "telephone-numbers": {
      "anyOf": [
        {
          "$ref": "#/definitions/phone"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/phone"
          },
          "minItems": 2
        }
      ]
    },
    "URLs": {
      "anyOf": [
        {
          "$ref": "#/definitions/url"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/url"
          },
          "minItems": 2
        }
      ]
    },
    "properties": {
      "anyOf": [
        {
          "$ref": "#/definitions/prop"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/prop"
          },
          "minItems": 2
        }
      ]
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
      "anyOf": [
        {
          "$ref": "#/definitions/link"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/link"
          },
          "minItems": 2
        }
      ]
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "org-name"
  ],
  "additionalProperties": false
}
```
- **Organization Identifier**: An identifier for an organization using a designated scheme.
```json
{
  "title": "Organization Identifier",
  "description": "An identifier for an organization using a designated scheme.",
  "$id": "#/definitions/org-id",
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
    "id"
  ],
  "additionalProperties": false
}
```
- **Organization Name**: Full (legal) name of an organization
```json
{
  "title": "Organization Name",
  "description": "Full (legal) name of an organization",
  "$id": "#/definitions/org-name",
  "type": "string"
}
```
- **OSCAL version**: OSCAL model version.
```json
{
  "title": "OSCAL version",
  "description": "OSCAL model version.",
  "$id": "#/definitions/oscal-version",
  "type": "string"
}
```
- **Party (organization or person)**: A responsible entity, either singular (an organization or person) or collective (multiple persons)
```json
{
  "title": "Party (organization or person)",
  "description": "A responsible entity, either singular (an organization or person) or collective (multiple persons)",
  "$id": "#/definitions/party",
  "type": "object",
  "properties": {
    "id": {
      "title": "Identifier",
      "description": "Unique identifier of the containing object",
      "type": "string"
    },
    "persons": {
      "anyOf": [
        {
          "$ref": "#/definitions/person"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/person"
          },
          "minItems": 2
        }
      ]
    },
    "org": {
      "$ref": "#/definitions/org"
    },
    "properties": {
      "anyOf": [
        {
          "$ref": "#/definitions/prop"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/prop"
          },
          "minItems": 2
        }
      ]
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
      "anyOf": [
        {
          "$ref": "#/definitions/link"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/link"
          },
          "minItems": 2
        }
      ]
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "additionalProperties": false
}
```
- **Party Reference**: References a party defined in metadata.
```json
{
  "title": "Party Reference",
  "description": "References a party defined in metadata.",
  "$id": "#/definitions/party-id",
  "type": "string"
}
```
- **Person**: A person, with contact information
```json
{
  "title": "Person",
  "description": "A person, with contact information",
  "$id": "#/definitions/person",
  "type": "object",
  "properties": {
    "person-name": {
      "$ref": "#/definitions/person-name"
    },
    "short-name": {
      "$ref": "#/definitions/short-name"
    },
    "org-name": {
      "$ref": "#/definitions/org-name"
    },
    "person-ids": {
      "anyOf": [
        {
          "$ref": "#/definitions/person-id"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/person-id"
          },
          "minItems": 2
        }
      ]
    },
    "organization-ids": {
      "anyOf": [
        {
          "$ref": "#/definitions/org-id"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/org-id"
          },
          "minItems": 2
        }
      ]
    },
    "addresses": {
      "anyOf": [
        {
          "$ref": "#/definitions/address"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/address"
          },
          "minItems": 2
        }
      ]
    },
    "email-addresses": {
      "anyOf": [
        {
          "$ref": "#/definitions/email"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/email"
          },
          "minItems": 2
        }
      ]
    },
    "telephone-numbers": {
      "anyOf": [
        {
          "$ref": "#/definitions/phone"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/phone"
          },
          "minItems": 2
        }
      ]
    },
    "URLs": {
      "anyOf": [
        {
          "$ref": "#/definitions/url"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/url"
          },
          "minItems": 2
        }
      ]
    },
    "properties": {
      "anyOf": [
        {
          "$ref": "#/definitions/prop"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/prop"
          },
          "minItems": 2
        }
      ]
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
      "anyOf": [
        {
          "$ref": "#/definitions/link"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/link"
          },
          "minItems": 2
        }
      ]
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "additionalProperties": false
}
```
- **Personal Identifier**: An identifier for a person (such as an ORCID) using a designated scheme.
```json
{
  "title": "Personal Identifier",
  "description": "An identifier for a person (such as an ORCID) using a designated scheme.",
  "$id": "#/definitions/person-id",
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
    "id"
  ],
  "additionalProperties": false
}
```
- **Person Name**: Full (legal) name of an individual
```json
{
  "title": "Person Name",
  "description": "Full (legal) name of an individual",
  "$id": "#/definitions/person-name",
  "type": "string"
}
```
- **Telephone**: Contact number by telephone
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
- **Port Range**: Where applicable this is the IPv4 port range on which the service operates.
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
- **Postal Code**: Postal or ZIP code for mailing address
```json
{
  "title": "Postal Code",
  "description": "Postal or ZIP code for mailing address",
  "$id": "#/definitions/postal-code",
  "type": "string"
}
```
- **Property**: A value with a name, attributed to the containing control, part, or group.
```json
{
  "title": "Property",
  "description": "A value with a name, attributed to the containing control, part, or group.",
  "$id": "#/definitions/prop",
  "type": "object",
  "properties": {
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
    }
  },
  "minProperties": 1,
  "maxProperties": 4
}
```
- **Protocol**: Information about the protocol used to provide a service.
```json
{
  "title": "Protocol",
  "description": "Information about the protocol used to provide a service.",
  "$id": "#/definitions/protocol",
  "type": "object",
  "properties": {
    "name": {
      "title": "Name",
      "description": "Identifying the purpose and intended use of the property, part or other object.",
      "type": "string"
    },
    "port-ranges": {
      "anyOf": [
        {
          "$ref": "#/definitions/port-range"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/port-range"
          },
          "minItems": 2
        }
      ]
    }
  },
  "additionalProperties": false
}
```
- **Publication Timestamp**: The date and time this document was published.
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
- **Purpose**: Describes the purpose for the service within the system.
```json
{
  "title": "Purpose",
  "description": "Describes the purpose for the service within the system.",
  "$id": "#/definitions/purpose",
  "type": "string"
}
```
- **Remarks**: Additional commentary on the parent item.
```json
{
  "title": "Remarks",
  "description": "Additional commentary on the parent item.",
  "$id": "#/definitions/remarks",
  "type": "string"
}
```
- **Remote Interconnected System Name**: The name of the remote interconnected system.
```json
{
  "title": "Remote Interconnected System Name",
  "description": "The name of the remote interconnected system.",
  "$id": "#/definitions/remote-system-name",
  "type": "string"
}
```
- **Resource**: A resource associated with the present document.
```json
{
  "title": "Resource",
  "description": "A resource associated with the present document.",
  "$id": "#/definitions/resource",
  "type": "object",
  "properties": {
    "id": {
      "title": "Identifier",
      "description": "Unique identifier of the containing object",
      "type": "string"
    },
    "desc": {
      "$ref": "#/definitions/desc"
    },
    "properties": {
      "anyOf": [
        {
          "$ref": "#/definitions/prop"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/prop"
          },
          "minItems": 2
        }
      ]
    },
    "rlinks": {
      "anyOf": [
        {
          "$ref": "#/definitions/rlink"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/rlink"
          },
          "minItems": 2
        }
      ]
    },
    "base64": {
      "$ref": "#/definitions/base64"
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "id"
  ],
  "additionalProperties": false
}
```
- **Responsible Party**: A reference to a set of organizations or persons that have responsibility for performing a referenced role relative to the parent context.
```json
{
  "title": "Responsible Party",
  "description": "A reference to a set of organizations or persons that have responsibility for performing a referenced role relative to the parent context.",
  "$id": "#/definitions/responsible-party",
  "type": "object",
  "properties": {
    "party-ids": {
      "anyOf": [
        {
          "$ref": "#/definitions/party-id"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/party-id"
          },
          "minItems": 2
        }
      ]
    },
    "properties": {
      "anyOf": [
        {
          "$ref": "#/definitions/prop"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/prop"
          },
          "minItems": 2
        }
      ]
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
      "anyOf": [
        {
          "$ref": "#/definitions/link"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/link"
          },
          "minItems": 2
        }
      ]
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "required": [
    "party-ids"
  ],
  "additionalProperties": false
}
```
- **Responsible Role**: A reference to one or more roles with responsibility for performing a function relative to the control.
```json
{
  "title": "Responsible Role",
  "description": "A reference to one or more roles with responsibility for performing a function relative to the control.",
  "$id": "#/definitions/responsible-role",
  "type": "object",
  "properties": {
    "properties": {
      "anyOf": [
        {
          "$ref": "#/definitions/prop"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/prop"
          },
          "minItems": 2
        }
      ]
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
      "anyOf": [
        {
          "$ref": "#/definitions/link"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/link"
          },
          "minItems": 2
        }
      ]
    },
    "party-ids": {
      "anyOf": [
        {
          "$ref": "#/definitions/party-id"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/party-id"
          },
          "minItems": 2
        }
      ]
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "additionalProperties": false
}
```
- **Resource link**: A pointer to an external copy of a document with optional hash for verification
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
      "anyOf": [
        {
          "$ref": "#/definitions/hash"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/hash"
          },
          "minItems": 2
        }
      ]
    }
  },
  "required": [
    "href"
  ],
  "additionalProperties": false
}
```
- **Role**: Defining a role to be assigned to a party
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
      "anyOf": [
        {
          "$ref": "#/definitions/prop"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/prop"
          },
          "minItems": 2
        }
      ]
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
      "anyOf": [
        {
          "$ref": "#/definitions/link"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/link"
          },
          "minItems": 2
        }
      ]
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
- **Role Identifier Reference**: A reference to the roles served by the user.
```json
{
  "title": "Role Identifier Reference",
  "description": "A reference to the roles served by the user.",
  "$id": "#/definitions/role-id",
  "type": "string"
}
```
- **Security Impact Level**: The overall level of expected impact resulting from unauthorized disclosure, modification, or loss of access to information.
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
- **Security Objective: Availability**: A target-level of availability for the system, based on the sensitivity of information within the system.
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
- **Security Objective: Confidentiality**: A target-level of confidentiality for the system, based on the sensitivity of information within the system.
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
- **Security Objective: Integrity**: A target-level of integrity for the system, based on the sensitivity of information within the system.
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
- **Security Sensitivity Level**: The overall information system sensitivity categorization, such as defined by FIPS-199.
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
- **Selected Level (Confidentiality, Integrity, or Availability)**: The selected (Confidentiality, Integrity, or Availability) security impact level.
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
- **Service**: Information about an individual service within the system.
```json
{
  "title": "Service",
  "description": "Information about an individual service within the system.",
  "$id": "#/definitions/service",
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
    "description": {
      "$ref": "#/definitions/description"
    },
    "properties": {
      "anyOf": [
        {
          "$ref": "#/definitions/prop"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/prop"
          },
          "minItems": 2
        }
      ]
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
      "anyOf": [
        {
          "$ref": "#/definitions/link"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/link"
          },
          "minItems": 2
        }
      ]
    },
    "ssp-protocol": {
      "anyOf": [
        {
          "$ref": "#/definitions/protocol"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/protocol"
          },
          "minItems": 2
        }
      ]
    },
    "purpose": {
      "$ref": "#/definitions/purpose"
    },
    "remarks": {
      "$ref": "#/definitions/remarks"
    }
  },
  "additionalProperties": false
}
```
- **Set Parameter Value**: Identifies the parameter that will be filled in by the enclosed value element.
```json
{
  "title": "Set Parameter Value",
  "description": "Identifies the parameter that will be filled in by the enclosed value element.",
  "$id": "#/definitions/set-param",
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
- **short-name**: A common name, short name or acronym
```json
{
  "title": "short-name",
  "description": "A common name, short name or acronym",
  "$id": "#/definitions/short-name",
  "type": "string"
}
```
- **State**: State, province or analogous geographical region for mailing address
```json
{
  "title": "State",
  "description": "State, province or analogous geographical region for mailing address",
  "$id": "#/definitions/state",
  "type": "string"
}
```
- **Specific Statement**: Identifies which statements within a control are addressed.
```json
{
  "title": "Specific Statement",
  "description": "Identifies which statements within a control are addressed.",
  "$id": "#/definitions/statement",
  "type": "object",
  "properties": {
    "description": {
      "$ref": "#/definitions/description"
    },
    "properties": {
      "anyOf": [
        {
          "$ref": "#/definitions/prop"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/prop"
          },
          "minItems": 2
        }
      ]
    },
    "links": {
      "anyOf": [
        {
          "$ref": "#/definitions/link"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/link"
          },
          "minItems": 2
        }
      ]
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
  "additionalProperties": false
}
```
- **Status**: Describes the operational status of the system.
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
- **System Characteristics**: Contains the characteristics of the system, such as its name, purpose, and security impact level.
```json
{
  "title": "System Characteristics",
  "description": "Contains the characteristics of the system, such as its name, purpose, and security impact level.",
  "$id": "#/definitions/system-characteristics",
  "type": "object",
  "properties": {
    "system-ids": {
      "anyOf": [
        {
          "$ref": "#/definitions/system-id"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/system-id"
          },
          "minItems": 2
        }
      ]
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
      "anyOf": [
        {
          "$ref": "#/definitions/prop"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/prop"
          },
          "minItems": 2
        }
      ]
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
      "anyOf": [
        {
          "$ref": "#/definitions/link"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/link"
          },
          "minItems": 2
        }
      ]
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
    "leveraged-authorizations": {
      "anyOf": [
        {
          "$ref": "#/definitions/leveraged-authorization"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/leveraged-authorization"
          },
          "minItems": 2
        }
      ]
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
- **System Identification**: A unique identifier for the system described by this system security plan.
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
- **System Implementation**: Provides information as to how the system is implemented.
```json
{
  "title": "System Implementation",
  "description": "Provides information as to how the system is implemented.",
  "$id": "#/definitions/system-implementation",
  "type": "object",
  "properties": {
    "properties": {
      "anyOf": [
        {
          "$ref": "#/definitions/prop"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/prop"
          },
          "minItems": 2
        }
      ]
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
      "anyOf": [
        {
          "$ref": "#/definitions/link"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/link"
          },
          "minItems": 2
        }
      ]
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
    "services": {
      "anyOf": [
        {
          "$ref": "#/definitions/service"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/service"
          },
          "minItems": 2
        }
      ]
    },
    "ssp-interconnection": {
      "anyOf": [
        {
          "$ref": "#/definitions/interconnection"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/interconnection"
          },
          "minItems": 2
        }
      ]
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
- **System Information**: Contains details about all information types that are stored, processed, or transmitted by the system, such as privacy information, and those defined in NIST SP 800-60.
```json
{
  "title": "System Information",
  "description": "Contains details about all information types that are stored, processed, or transmitted by the system, such as privacy information, and those defined in NIST SP 800-60.",
  "$id": "#/definitions/system-information",
  "type": "object",
  "properties": {
    "properties": {
      "anyOf": [
        {
          "$ref": "#/definitions/prop"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/prop"
          },
          "minItems": 2
        }
      ]
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
      "anyOf": [
        {
          "$ref": "#/definitions/link"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/link"
          },
          "minItems": 2
        }
      ]
    },
    "information-types": {
      "anyOf": [
        {
          "$ref": "#/definitions/information-type"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/information-type"
          },
          "minItems": 2
        }
      ]
    }
  },
  "required": [
    "information-types"
  ],
  "additionalProperties": false
}
```
- **System Inventory**: A set of inventory-item entries that represent the managed inventory instances of the system.
```json
{
  "title": "System Inventory",
  "description": "A set of inventory-item entries that represent the managed inventory instances of the system.",
  "$id": "#/definitions/system-inventory",
  "type": "object",
  "properties": {
    "inventory-items": {
      "anyOf": [
        {
          "$ref": "#/definitions/inventory-item"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/inventory-item"
          },
          "minItems": 2
        }
      ]
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
- **System Name (Full)**: The full name of the system.
```json
{
  "title": "System Name (Full)",
  "description": "The full name of the system.",
  "$id": "#/definitions/system-name",
  "type": "string"
}
```
- **System Name (Short)**: A short name for the system, such as an acronym, that is suitable for display in a data table or summary list.
```json
{
  "title": "System Name (Short)",
  "description": "A short name for the system, such as an acronym, that is suitable for display in a data table or summary list.",
  "$id": "#/definitions/system-name-short",
  "type": "string"
}
```
- **System Security Plan (SSP)**: A system security plan, such as those described in NIST SP 800-18
```json
{
  "title": "System Security Plan (SSP)",
  "description": "A system security plan, such as those described in NIST SP 800-18",
  "$id": "#/definitions/system-security-plan",
  "type": "object",
  "properties": {
    "id": {
      "title": "Identifier",
      "description": "Unique identifier of the containing object",
      "type": "string"
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
    "id",
    "import-profile",
    "system-characteristics"
  ],
  "additionalProperties": false
}
```
- **Citation target**: An address for retrieval of a citation
```json
{
  "title": "Citation target",
  "description": "An address for retrieval of a citation",
  "$id": "#/definitions/target",
  "type": "string"
}
```
- **Title**: A title for display and navigation
```json
{
  "title": "Title",
  "description": "A title for display and navigation",
  "$id": "#/definitions/title",
  "type": "string"
}
```
- **URL**: URL for web site or Internet presence
```json
{
  "title": "URL",
  "description": "URL for web site or Internet presence",
  "$id": "#/definitions/url",
  "type": "string",
  "format": "uri"
}
```
- **System User Class**: A type of user that interacts with the system based on an associated role.
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
      "anyOf": [
        {
          "$ref": "#/definitions/prop"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/prop"
          },
          "minItems": 2
        }
      ]
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
      "anyOf": [
        {
          "$ref": "#/definitions/link"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/link"
          },
          "minItems": 2
        }
      ]
    },
    "role-ids": {
      "anyOf": [
        {
          "$ref": "#/definitions/role-id"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/role-id"
          },
          "minItems": 2
        }
      ]
    },
    "authorized-privileges": {
      "anyOf": [
        {
          "$ref": "#/definitions/authorized-privilege"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/authorized-privilege"
          },
          "minItems": 2
        }
      ]
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
- **Value**: The phrase or string that fills-in the parameter and completes the requirement statement.
```json
{
  "title": "Value",
  "description": "The phrase or string that fills-in the parameter and completes the requirement statement.",
  "$id": "#/definitions/value",
  "type": "string"
}
```
- **Document version**: The version of the document content.
```json
{
  "title": "Document version",
  "description": "The version of the document content.",
  "$id": "#/definitions/version",
  "type": "string"
}
```


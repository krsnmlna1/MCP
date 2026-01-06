import json
from pathlib import Path
from jinja2 import Template

REACT_COMPONENT_TEMPLATE = """import React from 'react';

interface {{ component_name }}Props {
  {%- if props %}
  {% for prop in props %}
  {{ prop.name }}: {{ prop.type }};
  {%- endfor %}
  {%- endif %}
}

export const {{ component_name }}: React.FC<{{ component_name }}Props> = (props) => {
  return (
    <div className="{{ component_name_lower }}">
      <h2>{{ component_name }} Component</h2>
      {/* Add your content here */}
    </div>
  );
};

export default {{ component_name }};
"""

VUE_COMPONENT_TEMPLATE = """<template>
  <div class="{{ component_name_lower }}">
    <h2>{{ component_name }} Component</h2>
    {%- if props %}
    <p v-for="prop in {{ props_list }}" :key="prop">{{ '{{ prop }}' }}</p>
    {%- endif %}
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: '{{ component_name }}',
  {%- if props %}
  props: {
  {%- for prop in props %}
    {{ prop.name }}: {
      type: {{ prop.vue_type }},
      required: true,
    },
  {%- endfor %}
  },
  {%- endif %}
});
</script>

<style scoped>
.{{ component_name_lower }} {
  padding: 1rem;
}
</style>
"""

HTML_COMPONENT_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{{ component_name }}</title>
  <style>
    .{{ component_name_lower }} {
      padding: 1rem;
      font-family: Arial, sans-serif;
    }
  </style>
</head>
<body>
  <div class="{{ component_name_lower }}">
    <h2>{{ component_name }} Component</h2>
    {%- if description %}
    <p>{{ description }}</p>
    {%- endif %}
  </div>
</body>
</html>
"""


def generate_component(
    component_name: str,
    framework: str = "react",
    props: str = None,
    description: str = None
) -> str:
    """
    Generate a component boilerplate.
    
    Args:
        component_name: Name of the component (PascalCase)
        framework: 'react', 'vue', or 'html'
        props: JSON string of props [{\"name\": \"prop1\", \"type\": \"string\"}, ...]
        description: Brief description of the component
    """
    try:
        # Validate component name
        if not component_name or not component_name[0].isupper():
            return json.dumps({
                "status": "error",
                "message": "Component name must be PascalCase (e.g., MyComponent)"
            })
        
        # Parse props if provided
        parsed_props = []
        if props:
            try:
                parsed_props = json.loads(props)
            except json.JSONDecodeError:
                return json.dumps({
                    "status": "error",
                    "message": "Invalid props JSON format"
                })
        
        context = {
            "component_name": component_name,
            "component_name_lower": component_name.lower(),
            "props": parsed_props,
            "description": description or "",
            "props_list": ", ".join([p["name"] for p in parsed_props]) if parsed_props else ""
        }
        
        # Select template based on framework
        if framework.lower() == "react":
            template_str = REACT_COMPONENT_TEMPLATE
        elif framework.lower() == "vue":
            template_str = VUE_COMPONENT_TEMPLATE
        elif framework.lower() == "html":
            template_str = HTML_COMPONENT_TEMPLATE
        else:
            return json.dumps({
                "status": "error",
                "message": f"Unsupported framework: {framework}. Use 'react', 'vue', or 'html'"
            })
        
        template = Template(template_str)
        generated_code = template.render(**context)
        
        return json.dumps({
            "status": "success",
            "framework": framework,
            "component_name": component_name,
            "code": generated_code,
            "filename": f"{component_name}.tsx" if framework == "react" else f"{component_name}.vue" if framework == "vue" else f"{component_name}.html"
        })
    
    except Exception as e:
        return json.dumps({
            "status": "error",
            "message": str(e)
        })

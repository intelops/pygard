# pygard
> pronounce as py guard. Gard in Welsh language = in English Guard. 

Validation framework based on pydantic (optional CEL as well). 
> Inspired by our own project, GenVal, to make a pydantic-based validation framework open-source and agnostic so that everyone can share validation policies. This framework can be extended to support CEL, Rego (OPA or not OPA), or any other technology of your interest. 

List of items to be done:
- Data Models and data types validator {POC Done}
- The actual data validator
- Flexibity to use the validators as decorator
- Implement pulling the policies from policyhub which are stored in github repo and save them in local cache.
- Implement pulling the policies from github container registry, only after verifying the policies as secure OCI artifact using cosign tool.
- Include appropriate error handling.
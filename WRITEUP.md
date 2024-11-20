# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

*For **both** a VM or App Service solution for the CMS app:*
- I choose App Service. Lightweight APIs tend to be well-suited to App Services over VMs, and won't approach the size limit for App Services very easily. Additionally, App Services cost less than VMs do

### Assess app changes that would change your decision.
- I use Virtual Machine if Handling the vast increase in the number of users, with separate, dedicated servers

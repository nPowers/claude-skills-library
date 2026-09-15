# Certificate Lifecycle Manager

## Description
Plan and produce certificate lifecycle strategies including issuance, renewal, rotation, revocation, and monitoring for environments using ACME (Let's Encrypt), AWS ACM, or Vault. Use this skill to create rotation playbooks, sample automation scripts, alerting rules, and IaC snippets.

## Platforms
- Claude Desktop: Supported
- Claude Code: Not Supported

## Instructions
1. Ask which certificate authorities and tooling are in use (e.g., Let's Encrypt/certbot, AWS ACM, HashiCorp Vault), and whether certificates are for TLS, internal services, or code signing.
2. Collect rotation requirements: renewal window (days before expiry), allowed downtime, certificate distribution targets (load balancers, containers, secrets stores), and whether automated validation (HTTP-01, DNS-01) is available.
3. Produce a step-by-step rotation playbook tailored to the environment, including test/staging steps, rollback procedures, and post-rotation verification checks.
4. Provide example automation artifacts: certbot commands or hooks, sample ACME DNS automation snippets, Vault CLI/API calls or Terraform examples for ACM/Vault, and a sample CI/CD job that performs rotation and distribution.
5. Suggest monitoring and alerting rules (e.g., Prometheus alerting, CloudWatch alarms) to detect approaching expirations, and include a list of required permissions and secret-handling best practices.

## Example Usage
- "Create a certificate rotation playbook for services behind an ALB using AWS ACM"
- "Show me a certbot + DNS API script for issuing and renewing wildcard certificates"
- "What monitoring alerts should I add to catch certificates expiring within 30 days?"

## Note
The skill produces plans, scripts, and commands but does not store or manipulate secrets. Test any automation in a staging environment and ensure secure handling of private keys and API credentials.

"""Constants for the commands
"""

# Dump debugging details about the worker processes and threads
WORKERS_DEBUG = 'workers-debug'

# Router commands expect a 'router_id' argument in the payload with
# the UUID of the router

# Put a router in debug/manage mode
ROUTER_DEBUG = 'router-debug'
ROUTER_MANAGE = 'router-manage'
# Send an updated config to the router whether it is needed or not
ROUTER_UPDATE = 'router-update'

# Put a tenant in debug/manage mode
# Expects a 'tenant_id' argument in the payload with the UUID of the tenant
TENANT_DEBUG = 'tenant-debug'
TENANT_MANAGE = 'tenant-manage'

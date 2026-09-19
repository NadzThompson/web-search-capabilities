@description('Region for NOVA Web Search resources')
param location string = resourceGroup().location
param prefix string = 'nova-web-search'

resource storage 'Microsoft.Storage/storageAccounts@2023-05-01' = {
  name: uniqueString(resourceGroup().id, prefix)
  location: location
  sku: { name: 'Standard_GRS' }
  kind: 'StorageV2'
  properties: {
    allowBlobPublicAccess: false
    minimumTlsVersion: 'TLS1_2'
    supportsHttpsTrafficOnly: true
  }
}

resource logAnalytics 'Microsoft.OperationalInsights/workspaces@2023-09-01' = {
  name: '${prefix}-logs'
  location: location
  properties: { retentionInDays: 90 }
}

output storageAccountName string = storage.name
output logAnalyticsId string = logAnalytics.id

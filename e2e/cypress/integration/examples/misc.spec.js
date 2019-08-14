/// <reference types="Cypress" />

function createIndex(name, shards=12, replicas=1) {
  cy.request({
    method: 'POST',
    url: '/api/v1/rest/query', body: {
      body: {"settings": {"index": {"number_of_shards": shards,"number_of_replicas": replicas}}},
      path: `/${name}`,
      method: 'PUT'
    },
    headers: {'x-elastic-cluster': 'es-primary'}})
}

function deleteIndex(name){
  cy.request({
    method: 'POST',
    url: '/api/v1/rest/query', body: {path: `/${name}`,method: 'DELETE', body:{}},
    headers: { 'x-elastic-cluster': 'es-primary' }
  })
}

context('Misc', () => {
  beforeEach(() => {
    cy.server()
    deleteIndex('test*')
    deleteIndex('.special-index')
    cy.route('/api/v1/clients').as('getClients')
    cy.route('/api/v1/cluster/info/*').as('clusterInfo')
    cy.route('/api/v1/views/shards_grid').as('shardsGrid')
    cy.route('/api/v1/index/testindex/dynamicSettings').as('indexSettings')
    cy.route('POST', '/api/v1/index/testindex/settings').as('postSettings')
    cy.visit('/')
    cy.wait(['@getClients', '@clusterInfo'])
    cy.get('.cluster[data-cluster="es-primary"]').click()
    cy.wait('@shardsGrid')
  })
  describe('Filters', () => {
    it('Should filter special indices', () => {
      createIndex('.special-index', 12, 0)
      cy.get('[data-index-name=".special-index"]').should('exist')
      cy.get('[data-cy="show-hidden"]').click({force: true})
      cy.get('[data-index-name=".special-index"]').should('not.exist')
      deleteIndex('.special-index')
    })
  })
  describe('Change settings', () => {
    it('Should add replicas', () => {
      createIndex('testindex', 12, 0)
      cy.get('.index-name[data-index-name="testindex"]').click()
      cy.get('[data-tile="edit-settings"]').click()
      cy.wait(['@indexSettings', '@shardsGrid'])
      cy.get('[data-tab="dynamic-index settings"]').click()
      cy.get('[data-input="index.number_of_replicas"]').clear().type(1).blur()
      cy.get('[data-btn="save"]:not(.v-btn--disabled)').click()
      cy.wait('@postSettings')
      deleteIndex('testIndex')
    })
  })
  describe('Relocate shard', () => {
    it('cy.screenshot() - take a screenshot', () => {
      createIndex('testindex2', 12, 0)
      cy.get('.shard-square[data-node="node-1"][data-index="testindex2"]').eq(1).click()
      cy.get('[data-cy="toggle-relocation"]').click()
      cy.get('.node-name[data-node="node-2"]').click()
      cy.get('[data-cy="relocate-to-node"]').click()
      deleteIndex('testindex2')
    })
  })
})
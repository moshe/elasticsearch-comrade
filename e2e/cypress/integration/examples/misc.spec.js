/// <reference types="Cypress" />

context('Misc', () => {
  beforeEach(() => {
    cy.server()
    cy.request({
      method: 'POST',
      url: '/api/v1/rest/query', body: {path: '/testindex',method: 'DELETE', body:{}},
      headers: { 'x-elastic-cluster': 'es-primary' }
    })
    cy.route('/api/v1/clients').as('getClients')
      cy.request({
        method: 'POST',
        url: '/api/v1/rest/query', body: {
          body: {"settings": {"index": {"number_of_shards": 12,"number_of_replicas": 0}}},
          path: '/testindex',
          method: 'PUT'
        },
        headers: {'x-elastic-cluster': 'es-primary'}})
    cy.route('/api/v1/cluster/info/*').as('clusterInfo')
    cy.route('/api/v1/views/shards_grid').as('shardsGrid')
    cy.route('/api/v1/index/testindex/dynamicSettings').as('indexSettings')
    cy.route('POST', '/api/v1/index/testindex/settings').as('postSettings')
    cy.visit('/')
    cy.wait(['@getClients', '@clusterInfo'])
    cy.get('.cluster[data-cluster="es-primary"]').click()
    cy.wait('@shardsGrid')
  })
  describe('Change settings', () => {
    it('Should add replicas', () => {
      cy.get('.index-name[data-index-name="testindex"]').click()
      cy.get('[data-tile="edit-settings"]').click()
      cy.wait(['@indexSettings', '@shardsGrid'])
      cy.get('[data-tab="dynamic-index settings"]').click()
      cy.get('[data-input="index.number_of_replicas"]').clear().type(3).blur()
      cy.get('[data-btn="save"]').eq(1).click()
      cy.wait('@postSettings')
      cy.get('[data-input="index.number_of_replicas"]').clear().type(0).blur()
      cy.get('[data-btn="save"]').eq(1).click()
      cy.wait('@postSettings')
    })
  })
  describe('Relocate shard', () => {
    it('cy.screenshot() - take a screenshot', () => {
      cy.get('.shard-square[data-node="node-1"]').eq(1).click()
      cy.get('[data-cy="toggle-relocation"]').click()
      cy.get('.node-name[data-node="node-2"]').click()
      cy.get('[data-cy="relocate-to-node"]').click()
    })
  })
})
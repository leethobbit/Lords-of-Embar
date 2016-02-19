from robber import expect


def test_index_page_returns_html(server):
    response = server.get('/')

    expect(response.status).to.eq('200 OK')
    expect(response.status_int).to.eq(200)
    expect(response.content_type).to.eq('text/html')
    expect(response.content_length).to.be.above(0)

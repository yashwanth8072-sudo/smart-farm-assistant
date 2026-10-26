def test_health(client):
    r = client.get('/api/health')
    assert r.status_code == 200
    assert r.json()['status'] == 'ok'

def test_create_reading(client):
    r = client.post('/api/readings', json={'device_id':'soil-1','soil_moisture':20,'temperature_c':28,'humidity_pct':60})
    assert r.status_code == 201
    assert r.json()['soil_moisture'] == 20
    assert client.get('/api/readings').json()[0]['device_id'] == 'soil-1'

def test_invalid_moisture_rejected(client):
    r = client.post('/api/readings', json={'device_id':'soil-1','soil_moisture':120,'temperature_c':28,'humidity_pct':60})
    assert r.status_code == 422

def test_create_event(client):
    r = client.post('/api/events', json={'device_id':'cam-1','event_type':'motion_detected','confidence':0.8,'zone':'north'})
    assert r.status_code == 201
    assert r.json()['zone'] == 'north'

def test_irrigation_recommendation(client):
    client.post('/api/readings', json={'device_id':'soil-1','soil_moisture':15,'temperature_c':28,'humidity_pct':60})
    r = client.get('/api/irrigation/recommendation?threshold=30')
    assert r.status_code == 200
    assert r.json()['recommendation'] == 'check_irrigation'

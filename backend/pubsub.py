from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration

pnconfig = PNConfiguration()
pnconfig.subscribe_key = 'sub-c-c3382c1a-b7dc-11eb-8cd6-ee35b8e5702f'
pnconfig.publish_key = 'pub-c-f68a851e-fac5-496f-847d-9367777658d4'
pubnub = PubNub(pnconfig)

TEST_CHANNEL = 'TEST_CHANNEL'

pubnub.subscribe().channels([TEST_CHANNEL]).execute()

pubnub.add_listener()

def main():
    pubnub.publish().channel(TEST_CHANNEL).message({ 'awe': 'foo' }).sync()
    
if __name__ == '__main__':
    main()

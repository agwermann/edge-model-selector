import sys
from cloudevent import CloudEventService

if(len(sys.argv) < 2):
    print('Missing argument: please inform the broker address')
    exit()

broker_address = sys.argv[1]
source = "edge-controller"
message_type = "edge-to-cloud-model"
data = { "fed_model": "edge-model-file" }

#broker_address = 'http://localhost:8080'
#broker_address = "broker-ingress.knative-eventing.svc.cluster.local/fedlearning/default"

event = CloudEventService()
event.send_message(broker_address, source, message_type, data)
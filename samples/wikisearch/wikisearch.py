import wikipedia
import argparse
import json

output = {

}

parser = argparse.ArgumentParser(description='Page Downloader as PDF')
parser.add_argument('--question', '-q', action='store', dest='question',
                    required=True, help='Inform the link to download.')

arguments = parser.parse_args()
ques = arguments.question
ques = ques.replace(";", " ")
try:
  wikipedia.set_lang("en")
  output["message"] = wikipedia.summary(ques, sentences=3)
except Exception as ex:
  output["error"] = ex.message

print(json.dumps(output))
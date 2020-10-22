import dialogflow_v2 as dialogflow
import os

def dialogflow_setting():
  GOOGLE_AUTHENTICATION_FILE_NAME = "kobaksa.json"
  current_directory = os.path.dirname(os.path.realpath(__file__))
  path = os.path.join(current_directory, GOOGLE_AUTHENTICATION_FILE_NAME)
  os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = path
  intents_client = dialogflow.IntentsClient()
  parent = intents_client.project_agent_path('kobaksa-1b59d')

def create_intent():
  dialogflow_setting()

  part = dialogflow.types.Intent.TrainingPhrase.Part(
    text = "유소영의 테스트")
  training_phrase = dialogflow.types.Intent.TrainingPhrase(parts=[part])

  messages = []

  #이게 default message
  text = dialogflow.types.Intent.Message.Text(text = ["First message2"])
  text_message = dialogflow.types.Intent.Message(text=text)
  messages.append(text_message)

  # 이미지로 답변 가능하도록
  image = dialogflow.types.Intent.Message.Image(image_uri="https://s3.amazonaws.com/com.niches.production/niche_pages/square_images/000/001/619/giantc/sous-vide-ribeye-white-bean-puree-17.jpg")
  image_message = dialogflow.types.Intent.Message(image=image)
  messages.append(image_message)

  # 요거는 빠른 대답 가능하도록!
  quick_reply = dialogflow.types.Intent.Message.QuickReplies(
      title="Reply Prompt",
      quick_replies=["reply1", "reply2"])
  quick_reply_message = dialogflow.types.Intent.Message(quick_replies=quick_reply)
  messages.append(quick_reply_message)


  intent = dialogflow.types.Intent(
      display_name = "Jason's New Intent",
      training_phrases = [training_phrase],
      messages = messages
  )

  response = intents_client.create_intent(parent, intent)

# 매개변수 설정해서 코드 수정 필요
# 해당 인텐트에 trainging phrases 추가하기
# 이와 같이 코드로 default 답을 수정 할 수도 있을듯
def update_intent():
  dialogflow_setting()

  intents=intents_client.list_intents(parent)
  intent_path=[
      intent.name for intent in intents
      if intent.display_name=="getDataFromMySQL"
  ]
  print(intent_path)
  training_phrases = []
  intent= intents_client.get_intent(intent_path[0], intent_view=dialogflow.enums.IntentView.INTENT_VIEW_FULL)
  #intent = intents_client.get_intent(intent_path[0])

  part = dialogflow.types.Intent.TrainingPhrase.Part(
      text = "업데이트 확인입니다!!!!")
  training_phrase = dialogflow.types.Intent.TrainingPhrase(parts=[part])
  training_phrases.append(training_phrase)
  # training_phrases가 여러개일 경우
  '''for training_phrases_part in training_phrases_parts:
        part = dialogflow.types.Intent.TrainingPhrase.Part(
            text=training_phrases_part)
        training_phrase = dialogflow.types.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)'''
  intent.training_phrases.extend(training_phrases)
  response  = intents_client.update_intent(intent, language_code='ko')
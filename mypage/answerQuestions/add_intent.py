# -*- coding: utf-8 -*-
import dialogflow_v2 as dialogflow

intents_client = dialogflow.IntentsClient()
parent = intents_client.project_agent_path('kobaksa-1b59d')

training_phrases = []

training_phrases_parts = ['빨주노초파남보','12345','레드오렌지','맥북 사고싶어']

for training_phrases_part in training_phrases_parts:
        if "오렌지" in training_phrases_part:
            et = "@fruit:fruit"
        elif "맥북" in training_phrases_part:
            et = "@computer:computer"
        else: et = "@etc"

        part = dialogflow.types.Intent.TrainingPhrase.Part(text=training_phrases_part, entity_type=et)
        #part = dialogflow.types.Intent.TrainingPhrase.Part(text=training_phrases_part, entity_type='@sys.given-name', alias='name')
        # Here we create a new training phrase for each provided part.
        training_phrase = dialogflow.types.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)

#트레이닝 문구가 하나일 떄 
# part = dialogflow.types.Intent.TrainingPhrase.Part(text = "영미가 부른다.")
# training_phrase = dialogflow.types.Intent.TrainingPhrase(parts=[part])

messages = []

#default message 설정
text = dialogflow.types.Intent.Message.Text(text=["its working", "hey its great" ,"testing"])
text_message = dialogflow.types.Intent.Message(text=text)
# messages.append(text_message)

intent = dialogflow.types.Intent(
    display_name = "YM's New Intent",
    training_phrases=training_phrases,
    messages=[text_message],
    # webhook_state = 'WEBHOOK_STATE_ENABLED'
    # training_phrases = [training_phrase],
    # messages = messages
)


try:
    response = intents_client.create_intent(parent, intent)
    #response = client.create_entity_type(parent, entity_type)
except InvalidArgument:
    raise
# print('Intent created: {}'.format(response))



# # 이미지로 답변 가능하도록
# image = dialogflow.types.Intent.Message.Image(image_uri="https://s3.amazonaws.com/com.niches.production/niche_pages/square_images/000/001/619/giantc/sous-vide-ribeye-white-bean-puree-17.jpg")
# image_message = dialogflow.types.Intent.Message(image=image)
# messages.append(image_message)

# # 요거는 빠른 대답 가능하도록!
# quick_reply = dialogflow.types.Intent.Message.QuickReplies(
#     title="Reply Prompt",
#     quick_replies=["reply1", "reply2"])
# quick_reply_message = dialogflow.types.Intent.Message(quick_replies=quick_reply)
# messages.append(quick_reply_message)

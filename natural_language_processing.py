# pip install gTTS 
# pip install playsound


from gtts import gTTS
from playsound import playsound

#Natural Language Processing in Hindi

# Defining speech variable
user_speech = '''पिंकी बहुत प्यारी लड़की है। पिंकी कक्षा दूसरी में पढ़ती है।
एक दिन उसने अपनी किताब में रेलगाड़ी देखी। 
उसे अपनी रेल – यात्रा याद आ गई , जो कुछ दिन पहले पापा – मम्मी के साथ की थी।
पिंकी ने चौक उठाई और फिर क्या था , दीवार पर रेलगाड़ी का इंजन बना दिया।
उसमें पहला डब्बा जुड़ गया , दूसरा डब्बा जुड़ गया , जुड़ते – जुड़ते कई सारे डिब्बे जुड़ गए। 
जब चौक खत्म हो गया पिंकी उठी उसने देखा कक्षा के आधी दीवार पर रेलगाड़ी बन चुकी थी। 
फिर क्या हुआ  – रेलगाड़ी दिल्ली गई  ,  मुंबई गई   ,   अमेरिका गई  ,  नानी के घर गई ,  और दादाजी के घर भी गई।
मुझे अनिकेत गुप्ता द्वारा प्रोग्राम किया गया है। धन्यवाद अनिकेत '''

# Defining speech parameters for English Language
# objective = gTTS(text = user_speech, slow = False, lang = "en")


# Defining speech parameters for hindi language
objective = gTTS(text = user_speech, slow = False, lang = "hi")

# Saving the speech
objective.save("synthesis_hindi.mp3")

# Say it aloud
playsound("synthesis_hindi.mp3")
 

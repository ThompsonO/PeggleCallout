import screenshot
# Model built with python 3.10.6
import tensorflow as tf

model = tf.keras.models.load_model('model_adventure_11ep_color_scaled')

def can_fire():
    fireable = False

    img = screenshot.screenshot()
    img_array = tf.keras.preprocessing.image.img_to_array(img)

    img_array = tf.expand_dims(img_array, 0)
    
    prediction = model(img_array)

    #Can fire!
    if prediction[0][0] > prediction[0][1]:
        fireable = True

    return fireable


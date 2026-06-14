from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

import joblib
import os
import gradio as gr

## Load the trained model
model_path = os.path.join("models", "best_model.pkl")   

loaded_pipeline = joblib.load(model_path)

## Define the prediction function
def predict_house_price(income, house_age, rooms, bedrooms, population):
   
    # Make prediction using the loaded pipeline
    predicted_price = loaded_pipeline.predict(
        [[income, house_age, rooms, bedrooms, population]]
    )[0]

    return f"🏠 Estimated House Price\n\n${predicted_price:,.2f}"

## Create the Gradio interface
interface = gr.Interface(
    fn=predict_house_price,
    inputs=[
        gr.Number(
            label="Average Income ($)",
            info="Average income of residents in the area",
            value=70000
        ),
        gr.Slider(
            label="Average House Age (years)",
            minimum=0,
            maximum=20,
            step=1,
            value=7
        ),
        gr.Slider(
            label="Average Number of Rooms",
            minimum=1,
            maximum=15,
            step=0.5,
            value=5
        ),
        gr.Slider(
            label="Average Number of Bedrooms",
            minimum=1,
            maximum=10,
            step=0.5,
            value=3
        ),
        gr.Number(
            label="Area Population",
            info="Population of the area",
            value=25000
         )
        ],
    outputs=gr.Textbox(
        label="Predicted House Price"
    ),

    title="🏠 House Price Prediction System",

    description="""
Predict house prices using a machine learning model trained on housing data.

Enter the area characteristics below and click Submit to estimate the property value.
""",

    examples=[
        [79545.45, 5.68, 7.01, 4.09, 23086.80],
        [61287.06, 5.86, 8.51, 6.23, 40173.07],
        [63345.24, 7.18, 5.58, 3.09, 36882.15]
    ],
    theme=gr.themes.Soft(
    primary_hue="green",
    secondary_hue="orange",
)
)

interface.launch(share=True)
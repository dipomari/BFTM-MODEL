import streamlit as st
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline
from spacy import displacy

# Loadinf Fine tuned model and tokenizer
tokenizer = AutoTokenizer.from_pretrained('Ai-Application/Models/bftm')
model = AutoModelForTokenClassification.from_pretrained('Ai-Application/Models/bftm')

def visualize_entities(text, ner_result):

    #Colors for the visualization
    colors = {
    "B-ORG": "#ffcccc", 
    "I-ORG": "#ffcccc", 
    "B-LOC": "#99ff99",  
    "I-LOC": "#99ff99",  
    "B-YEAR": "#9999ff",  
    "B-BUDGET": "#ccccff", 
    "B-ALLOCATION": "#ffff99", 
    "I-BUDGET": "#ccccff",  
    "I-ALLOCATION": "#ffff99"  
}
    # Goin through the predictions putting tehm in the dic for displacy
    entities = []
    for entity in ner_result:
        e_dic = {"start": entity["start"], "end": entity["end"], "label": entity["entity"]}

        # Merging adjacent entities of the same type (GPT help)

        '''
        if entities and ...: This checks if the entities list is not empty and proceeds to the next condition only if it's not empty.

        -1 <= entity["start"] - entities[-1]["end"] <= 1: This condition checks if the difference between the start of the current entity 
        (entity["start"]) and the end of the previous entity in the list (entities[-1]["end"]) is within a range of -1 to 1. Essentially,
          it's checking if the current entity is adjacent or overlapping with the previous entity.


        entities[-1]["label"] == e_dic["label"]: This condition checks if the label of the current entity (e_dic["label"]) is the same as 
        the label of the previous entity in the list (entities[-1]["label"]). This is to ensure that we are dealing with entities of the 
        same type.
        '''

        if entities and -1 <= entity["start"] - entities[-1]["end"] <= 1 and entities[-1]["label"] == e_dic["label"]:
            entities[-1]["end"] = e_dic["end"]
            continue

        entities.append(e_dic)
    
    render_data = [{"text": text, "ents": entities}]
    visualization = displacy.render(render_data, style="ent", manual=True, options={"colors": colors})
    st.components.v1.html(visualization, width=800, height=600)


def main():
    st.title("Text Labeling Fine Tuned Model BFTM")

    # Default Text example
    default_text = "Das Budget für das Gesundheitsamt München wurde für das Jahr 2021 um 8 % auf insgesamt 25,6 Mio. € erhöht. Diese Steigerung ermöglicht eine bessere Ausstattung der medizinischen Einrichtungen sowie zusätzliche Maßnahmen zur Förderung der öffentlichen Gesundheit. Des Weiteren werden Mittel für die Beschaffung von medizinischem Equipment und die Finanzierung von Präventionsprogrammen bereitgestellt."

    text = st.text_area("Enter your German text here:", value=default_text, height=200)

    # When clicking button, the text goes to the tokenizer and then model for predictions
    if st.button("Label Text"):
        ner = pipeline("ner", model=model, tokenizer=tokenizer)
        ner_result = ner(text)

        # Predictions are sent to the visualization function
        st.subheader("Entity Visualization with spaCy:")
        visualize_entities(text, ner_result)

if __name__ == "__main__":
    main()

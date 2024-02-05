import streamlit as st

# Set the background color to black and text color to white
# st.markdown(
#     """
#     <style>
#         .stApp {
#             background-color: #000000; /* Black background */
#             color: #FFFFFF; /* White text */
#         }
#         h1, h2, h3, h4, h5, h6 {
#             color: #FFFFFF; /* White text for headers */strem
#         }
#         .markdown-text a {
#             color: #FFFFFF; /* White text for links */
        
#         }

#         .stSidebar {
#             background-color: #000000 !important; 
#             color: #FFFFFF
#         }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # Your Streamlit app content goes here
# st.title("Streamlit App")

# # Sidebar with buttons
# st.sidebar.title("Action")
# button1 = st.sidebar.button("Button 1")
# button2 = st.sidebar.button("Button 2")

# # Handle button clicks
# if button1:
#     st.write("Button 1 was clicked!")
# elif button2:
#     st.write("Button 2 was clicked!")

# # Main content
# st.write("This is a simple Streamlit app with a custom background color and white text.")
# st.header("This is a header")
# st.subheader("This is a subheader")
# st.markdown("This is a paragraph with [a link](https://example.com).")



# custom_palette = sns.color_palette("Set2", n_colors=len(df.property_type.unique()))
#         font_style = {'family': 'serif', 'color':  'darkred', 'weight': 'normal', 'size': 12}
        
       
#         plt.rcParams.update({'font.family': 'serif', 'font.serif': 'Times New Roman'})

#         plt.figure(figsize=(4, 2))
#         ax = sns.countplot(data=df, y=df.property_type.values, order=df.property_type.value_counts().index[:10],palette=custom_palette)
#         ax.set_title("Top 10 Property Types available",fontdict={'family': 'serif', 'color':  'darkblue', 'weight': 'normal', 'size': 7})
#         ax.set_xlabel("Count", fontdict=font_style,fontsize=6)
#         ax.set_ylabel("Property Type", fontdict=font_style,fontsize=6)
#         ax.tick_params(axis='x', labelsize=4)
#         ax.tick_params(axis='y', labelsize=4)
#         st.pyplot()

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from streamlit_option_menu import option_menu
from PIL import Image
import seaborn as sns
import matplotlib.pyplot as plt

icon = Image.open("airbnb.png")
st.set_page_config(page_title= "Airbnb analysis",
                   page_icon= icon,
                   layout= "wide",
                    initial_sidebar_state= "expanded"
                   )

df = pd.read_csv('airbnb_dataset.csv')

st.markdown("# :red[Airbnb Analysis]")
st.markdown("##")
# with st.headbar:
SELECT = option_menu(
    menu_title=None,
    options=["Home","Analyze","Contact"],
    icons=["house", "kanban", "mailbox"],
    default_index=2,
    orientation="horizontal",
    styles={"container": {"padding": "0!important", "background-color": "white", "size": "cover", "width": "80"},
            "icon": {"color": "black", "font-size": "20px"},

            "nav-link": {"font-size": "20px", "text-align": "center", "margin": "-2px", "--hover-color": "#FF5A5F"},
            "nav-link-selected": {"background-color": "#FF5A5F"}})



#tab1, tab2, tab3 = st.tabs(["🏠 Home","📈 Analyze","📧 Contact"])

if SELECT == "Home":

    
    st.markdown("## :red[Exploration and Analysis of Airbnb data]")
    col1,col2 = st.columns([2,2],gap="medium")
    with col1:
        st.markdown("##")
        st.image("airbnbbooking.png")
        text = """
                **Airbnb is an online marketplace that connects people who want to rent out their property with people who are looking for accommodations, typically for short stays..** 
                *Airbnb offers hosts a relatively easy way to earn some income from their property. Guests often find that Airbnb rentals are cheaper and homier than hotels*.
                """


        st.markdown(text, unsafe_allow_html=True)
        st.write("---")

    with col2:
        st.markdown("##")
        
        st.video("C:/Users/pkart/OneDrive/Desktop/phonepe/airbnbvdo.mp4")
    
    



#Data analyze
if SELECT == "Analyze":

    st.markdown("##")
    with st.sidebar:
        selected_tab = option_menu("Airbnb analysis", ["Review by Room","Review by City","Review by reviews"], 
                default_index=0,
                styles={"nav-link": {"font-size": "15px", "text-align": "left", "margin": "-1px", "--hover-color": "#FF5A5F"},
                        "nav-link-selected": {"background-color": "#FF5A5F"}})
    
    
    if selected_tab == 'Review by Room':
    
      

        #Availbility on room type
        rooms_avail = df.groupby(['room_type']).count().reset_index(0)
        rooms_avail = rooms_avail[['room_type','availability_30','availability_60','availability_90']] 
        st.dataframe(rooms_avail.style.background_gradient(cmap="Oranges"),width=900)



        col1,col2 = st.columns([2,2],gap="small")

        with col1:
                
                #Distribution of room type
                fig = px.pie(df,
                                    title='Distribution of room type',
                                    names='room_type',
                                    color='room_type',    
                                    color_discrete_sequence=px.colors.sequential.Agsunset)
                st.plotly_chart(fig,use_container_width=True) 

        with col2:
                
                #Night stays based on cities
                minimum_nit = df.groupby(['city','room_type'])['minimum_nights'].count().reset_index()
                minimum_nit = minimum_nit.sort_values(by='minimum_nights', ascending=False)
            
                fig = px.bar(minimum_nit,x='room_type', y='minimum_nights', color='room_type',
                            labels={'minimum_nights': 'Minimum number of nights stayed'},
                            title='Room type with Minimum no of stays', width=550, height=450)

                st.plotly_chart(fig)

                #Downloading data
                dwld_data = minimum_nit.to_csv(index=False).encode('utf-8')
                st.download_button("Download and view",dwld_data,"Night stays on cities.csv","text/csv",key="download-csv")


    elif selected_tab == 'Review by City':

        #Average price on cities
        st.header('Average Price on Cities')
        avg_price_per_city = df.groupby('city')['price'].mean().reset_index()
        fig = px.scatter(avg_price_per_city, x='city', y='price', color='city',
                    labels={'price': 'Average Price'},
                    width=700, height=450)
        st.plotly_chart(fig)
        

        #Map exploration for cities
        selected_city = st.selectbox('Select City', df['city'].unique())
        filtered_data = df[df['city'] == selected_city]
        
        try:
            
            st.header(f'Airbnb Listings in {selected_city}')
            fig = px.scatter_geo(filtered_data, 
                                lat='latitude', 
                                lon='longitude', 
                                color='price', 
                                size='accommodates',
                                hover_name='name',
                                title=f'Airbnb Listings in {selected_city}',
                                width=800,
                                height=600,
                                color_continuous_scale='Hot'
                                )
            fig.update_geos(
                            resolution=50,
                            showcoastlines=True, coastlinecolor="RebeccaPurple",
                            showland=True, landcolor="LightGreen",
                            showocean=True, oceancolor="LightBlue",
                            showlakes=True, lakecolor="Blue",
                            showrivers=True, rivercolor="Blue"
                            )
            fig.update_layout(height=600, margin={"r":0,"t":0,"l":0,"b":0})
            st.plotly_chart(fig)
            
            new_data= filtered_data[['price','name']]
            new_data.set_index('price',inplace=True)
            new_data = new_data.sort_values(by='price',ascending=False)

            #Downloading the report for price list
            dwld_data = new_data.to_csv(index=True).encode('utf-8')
            st.download_button("Download and view",dwld_data,"Price.csv","text/csv",key="download-csv")

        except Exception as e:
    
            st.error(f"An error occurred: {e}")
            st.write(filtered_data.head())

    elif selected_tab == 'Review by reviews':

        st.header('Reviews')
        rev_df = df.groupby('room_type')['review_scores_value'].mean().sort_values().reset_index()
        fig = px.line(rev_df, x='room_type', y='review_scores_value', title='Reviews on room type',
              labels={'room_type': 'Room Type', 'review_scores_value': 'Mean Review Scores'},
              width=700, height=450)
        
        #fig = px.bar(rev_df,x='room_type',y='review_scores_value',color='review_scores_value',title='Reviews on room type', width=700, height=450)
        st.plotly_chart(fig)

    

        top_property_types = df.groupby('property_type').agg({
                'review_scores_value': 'mean',
                'price': 'mean'
            }).sort_values(by='review_scores_value', ascending=False).head(10).reset_index()

            # Bar chart using Plotly Express
        fig = px.bar(top_property_types, x='property_type', y=['review_scores_value', 'price'],
                        labels={'value': 'Average'},
                        title='Top 10 Property Types Based on Review Scores and Price',
                        width=800, height=500)

       
        st.plotly_chart(fig)
    

if SELECT == "Contact":
        st.markdown("## :red[CONCLUSION]")
        col1, col2 =st.columns([3,2],gap="medium")
        with col1:
            st.image("pexels_airbnb.jpg")

            sentences = [
                            "The people who prefer to stay in Entire home or Apartment they are going to stay bit longer in that particular Neighbourhood only.",
                            "The people who prefer to stay in Private room they won't stay longer as compared to Home or Apartment.",
                            "Most people prefer to pay less price.",
                            "If people are not staying more then one night means they are travellers."
                        ]
            #st.write("### CONCLUSION:")
            for sentence in sentences:
                st.write(f"- *{sentence}*")

        with col2:
           
    
            name = "Data visualized by: Karthika P "
            mail = (f'{"Mail :"}  {"pkarthika923@gmail.com"}')
            social_media = {"GITHUB": "https://github.com/KarthikaPonnusamy ",
                            "LINKEDIN": "https://www.linkedin.com/in/karthika-p-863361277/"
                            }
            st.subheader(name)
            st.write(mail)
            
            cols = st.columns(len(social_media))
            for index, (platform, link) in enumerate(social_media.items()):
                cols[index].write(f"[{platform}]({link})")
import json                     # for saving and parsing json files
import matplotlib.pyplot        # for converting rgb to hex
import matplotlib.colors        # for getting pretty colors
import numpy                    # for generic operations
import os                       # for searching for json files
import pandas                   # dumping json into csv
import plotly.express           # plotly
import sentence_transformers    # embeddings
import sklearn.decomposition    # orient tsne
import sklearn.manifold         # make a tsne


# Identify all the json files
path_to_json: str = './data/'
json_files: list[str] = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

# Dump all the json files into a single dataframe
all_the_data: pandas.DataFrame = pandas.DataFrame()
for json_file in sorted(json_files, key=str.casefold):
    with open(os.path.join(path_to_json, json_file)) as json_file_path:
        json_dict: dict = json.load(json_file_path)
        json_as_df: pandas.DataFrame = pandas.DataFrame.from_dict(json_dict)
        json_as_df['faculty'] = json_file.replace(".json", "")
        all_the_data: pandas.DataFrame = pandas.concat([all_the_data, json_as_df], axis=0)

# Re-index the dataframe because it appears to eb necessary
all_the_data.reset_index(inplace=True)

# Embed titles from publications
model = sentence_transformers.SentenceTransformer('all-mpnet-base-v2')
embeddings: numpy.ndarray = model.encode(all_the_data['title'], show_progress_bar=True)

# Boil down teh data into a 2D plot
tsne_embeddings: numpy.ndarray = sklearn.manifold.TSNE(n_components=2, random_state=42).fit_transform(embeddings)
pca_embeddings: numpy.ndarray = sklearn.decomposition.PCA(n_components=2, random_state=42).fit_transform(tsne_embeddings)
all_the_data['x'] = pca_embeddings[:, 0]
all_the_data['y'] = pca_embeddings[:, 1]

# Make some pretty colors! 
colors: list[str] = [matplotlib.colors.to_hex(x) for x in matplotlib.pyplot.cm.gist_rainbow(numpy.linspace(0, 1, len(json_files)))]

# Plot the embeddings
fig = plotly.express.scatter(
    all_the_data,
    x="x",
    y="y",
    hover_data=["title"],
    color="faculty",
    symbol="faculty",
    color_discrete_sequence=colors
)

# Make sure the axes are appropriately scaled
fig.update_xaxes(
    visible=False,
    autorange=False,
    range=[numpy.min(pca_embeddings[:, 0]) * 1.05, numpy.max(pca_embeddings[:, 0]) * 1.05]
)

fig.update_yaxes(
    visible=False,
    scaleanchor="x",
    scaleratio=1,
    range=[numpy.min(pca_embeddings[:, 1]) * 1.05, numpy.max(pca_embeddings[:, 1]) * 1.05]
)

# Reset the layout
fig.update_layout(
    margin=dict(l=0, r=0, t=0, b=0),
    legend=dict(y=0.5),
    plot_bgcolor="#191C1F",
)

# Remove the logo
fig.show(config=dict(displaylogo=False))

# Save the file
fig.write_html("index.html")

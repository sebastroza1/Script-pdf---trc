from . import create_app

# ``create_app`` already knows where the templates folder is located,
# but we instantiate the application here so Flask's CLI can discover it.
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

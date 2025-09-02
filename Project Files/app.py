from flask import Flask, render_template, request, send_file
import csv
import io
from dblp_scraper import get_publications

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    author_name = request.form['author_name'].strip()
    publications = get_publications(author_name)

    if not publications:
        return render_template('results.html', author_name=author_name, publications=[], 
                               years=[], counts=[], summary="No publications found.")

    # Generate summaries for publications
    for pub in publications:
        title = pub.get("title", "No Title")
        authors = pub.get("authors", "Unknown Authors")
        year = pub.get("year", "N/A")
        venue = pub.get("venue", "Unknown Venue")
        abstract = pub.get("abstract", "").strip()

        pub["summary"] = abstract if abstract else (
            f'"{title}" was published in "{venue}" in {year}. '
            f'Authored by {authors}, this work offers key insights and contributions. '
            f'For more details, refer to the full text.'
        )

    # Count publications per year
    year_counts = {}
    for pub in publications:
        year = pub["year"]
        if year.isdigit():
            year_counts[year] = year_counts.get(year, 0) + 1

    sorted_years = sorted(year_counts.keys())
    publication_counts = [year_counts[year] for year in sorted_years]

    # Generate author's overall summary
    num_pubs = len(publications)
    valid_years = [int(pub["year"]) for pub in publications if pub["year"].isdigit()]
    overall_summary = (f"{author_name} has {num_pubs} publications spanning from {min(valid_years)} to {max(valid_years)}."
                        if valid_years else f"{author_name} has {num_pubs} publications.")

    return render_template('results.html', author_name=author_name, 
                           publications=publications, years=sorted_years, 
                           counts=publication_counts, summary=overall_summary)

@app.route('/featured')
def featured():
    publications = get_publications("latest")[:10]  # Fetch latest 10 publications
    return render_template('featured.html', publications=publications)

@app.route('/download_csv', methods=['POST'])
def download_csv():
    author_name = request.form['author_name']
    publications = get_publications(author_name)

    if not publications:
        return "No publications found for this author."

    output = io.StringIO()
    csv_writer = csv.writer(output)
    csv_writer.writerow(['Title', 'Summary', 'Year', 'Venue', 'DOI'])
    
    for pub in publications:
        csv_writer.writerow([
            pub.get('title', 'No Title'),
            pub.get('summary', 'No Summary'),
            pub.get('year', 'N/A'),
            pub.get('venue', 'Unknown Venue'),
            pub.get('doi', 'N/A')
        ])
    
    output.seek(0)
    return send_file(io.BytesIO(output.getvalue().encode()), mimetype='text/csv', as_attachment=True, download_name=f"{author_name}_publications.csv")

# Add this route to app.py
@app.route('/stats')
def stats():
    # In a real app, you would fetch actual statistics data here
    return render_template('stats.html')
@app.route('/news')
def news():
    return render_template('news.html')



if __name__ == '__main__':
    app.run(debug=True)

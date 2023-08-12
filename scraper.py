import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify

app = Flask(__name__)


def get_gold_prices():
    url = "http://goldtraders.or.th/UpdatePriceList.aspx"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        table = soup.find("table", {"id": "DetailPlace_MainGridView"})

        if table:
            data = []

            for row in table.find_all("tr")[1:]:
                columns = row.find_all("td")
                row_data = [column.text.strip() for column in columns]
                data.append(row_data)

            return data
        else:
            return None
    else:
        return None


@app.route("/gold_prices", methods=["GET"])
def gold_prices():
    gold_data = get_gold_prices()
    if gold_data:
        return jsonify(gold_data)
    else:
        return jsonify({"error": "Data not available"})


if __name__ == "__main__":
    app.run(debug=True)

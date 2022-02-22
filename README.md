# shoppingcart-2022

## Usage

```sh
python shopping_cart.py
```
## Email Functionlity 

### install dotenv
```sh 
pip install python-dotenv
```
### create an .env file
```sh
mkdir .env
```
### sign up for a SendGrid account then create an API Key with "full access" permissions. Store the API Key value in an environment variable called SENDGRID_API_KEY.
### also set an environment variable called SENDER_ADDRESS to be the same email address as the single sender address you just associated with your SendGrid account.

### 'Create Template' on Sendgrid

### Code Tab
```ssh
<img src="https://www.shareicon.net/data/128x128/2016/05/04/759867_food_512x512.png">

<h3>Hello this is your receipt</h3>

<p>Date: {{human_friendly_timestamp}}</p>

<ul>
{{#each products}}
	<li>You ordered: ... {{this.name}}</li>
{{/each}}
</ul>

<p>Total: {{total_price_usd}}</p>
```
### Test Data
{
    "total_price_usd": "$99.99",
    "human_friendly_timestamp": "July 4th, 2099 10:00 AM",
    "products":[
        {"id": 100, "name": "Product 100"},
        {"id": 200, "name": "Product 200"},
        {"id": 300, "name": "Product 300"},
        {"id": 200, "name": "Product 200"},
        {"id": 100, "name": "Product 100"}
    ]
}



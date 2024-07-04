import requests

# Function to search for the company's website using SerpAPI
def search_company_website(company_name, serpapi_key):
    params = {
        "q": company_name,
        "api_key": serpapi_key,
        "engine": "google",
        "num": "1"
    }
    response = requests.get("https://serpapi.com/search", params=params)
    results = response.json()
    return results['organic_results'][0]['link']

# Function to search for the CEO's name using SerpAPI
def search_ceo_name(company_name, serpapi_key):
    query = f"{company_name} CEO name"
    params = {
        "q": query,
        "api_key": serpapi_key,
        "engine": "google",
        "num": "1"
    }
    response = requests.get("https://serpapi.com/search", params=params)
    results = response.json()
    return results['organic_results'][0]['snippet']

# Function to search for the CEO's email using SerpAPI
def search_ceo_email(company_name, serpapi_key):
    query = f"{company_name} CEO email"
    params = {
        "q": query,
        "api_key": serpapi_key,
        "engine": "google",
        "num": "1"
    }
    response = requests.get("https://serpapi.com/search", params=params)
    results = response.json()
    return results['organic_results'][0]['snippet']

def main():
    serpapi_key = '796e561255c41d8d5f184718262804fb1eac3719b866b0558817faee168e9a2e'
    company_name = input("Enter the company name: ")

    # Step 1: Get company website link
    company_website = search_company_website(company_name, serpapi_key)
    print(f"Company Website: {company_website}")

    # Step 2: Get CEO's full name
    ceo_name = search_ceo_name(company_name, serpapi_key)
    print(f"CEO Name: {ceo_name}")

    # Step 3: Get CEO's email
    ceo_email = search_ceo_email(company_name, serpapi_key)
    print(f"CEO Email: {ceo_email}")

if __name__ == "__main__":
    main()

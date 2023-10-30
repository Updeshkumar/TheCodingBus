from django.shortcuts import render
# from django.http import HttpResponse
# import requests
# from .forms import URLForm  # Import your URLForm

# def index(request):
#     if request.method == 'POST':
#         form = URLForm(request.POST)
#         if form.is_valid():
#             url = form.cleaned_data['url']
#             headers = {
#                 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
#             }
#             response = requests.get(url, headers=headers)
#             if response.status_code == 200:
#                 html = response.text

#                 # Set the content type to force a file download
#                 response = HttpResponse(html, content_type='text/html')
#                 response['Content-Disposition'] = f'attachment; filename="downloaded.html"'

#                 return response
#             else:
#                 return HttpResponse(f"Failed to fetch the URL: {url}, Status Code: {response.status_code}")

#     else:
#         form = URLForm()

#     return render(request, 'your_template.html', {'form': form})

from django.http import HttpResponse
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os
import re 

def get_sitemap_url(robots_url):
    response = requests.get(robots_url)
    if response.status_code == 200:
        robots_content = response.text
        for line in robots_content.split('\n'):
            if line.startswith("Sitemap: "):
                return line.split("Sitemap: ")[1].strip()
    return None

def clone_website(request):
    if request.GET.get('download'):
        download_option = request.GET.get('download')

        if download_option == 'sitemap':
            # Attempt to fetch the sitemap URL from the website's robots.txt
            url = request.GET.get('url')
            if not url:
                return HttpResponse("Please provide a URL to clone.")

            robots_url = urljoin(url, '/robots.txt')
            sitemap_url = get_sitemap_url(robots_url)
            
            if sitemap_url:
                response = requests.get(sitemap_url)
                if response.status_code == 200:
                    sitemap_content = response.text
                    response = HttpResponse(sitemap_content, content_type='text/xml')
                    response['Content-Disposition'] = 'attachment; filename="sitemap.xml"'
                    return response

                return HttpResponse(f"Failed to fetch the sitemap: {sitemap_url}, Status Code: {response.status_code}")

            return HttpResponse("No sitemap found in the website's robots.txt.")

        if download_option == 'website':
            # Serve the cloned HTML file for download
            try:
                with open('your_template.html', 'r', encoding='utf-8') as html_file:
                    html_content = html_file.read()
                response = HttpResponse(html_content, content_type='text/html')
                response['Content-Disposition'] = 'attachment; filename="cloned_website.html"'
                return response

            except Exception as e:
                return HttpResponse(f"An error occurred: {str(e)}")

    if request.method == 'POST':
        url = request.POST.get('url')

        if not url:
            return HttpResponse("Please provide a URL to clone.")

        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
            }
            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                html_content = response.text

                # Create a BeautifulSoup object for parsing HTML
                soup = BeautifulSoup(html_content, 'html.parser')

                # Save the HTML content to a file
                with open('your_template.html', 'w', encoding='utf-8') as file:
                    file.write(soup.prettify())

                # Find and save linked CSS files (handle relative URLs)
                css_links = soup.find_all('link', rel='stylesheet')
                for link in css_links:
                    css_url = link.get('href')
                    if css_url:
                        # Convert relative URLs to absolute URLs
                        absolute_css_url = urljoin(url, css_url)
                        css_filename = re.sub(r'[?#].*$', '', os.path.basename(absolute_css_url))
                        css_response = requests.get(absolute_css_url)
                        if css_response.status_code == 200:
                            css_content = css_response.text
                            with open(css_filename, 'w', encoding='utf-8') as css_file:
                                css_file.write(css_content)

                return render(request, 'your_template.html')
            elif response.status_code == 403:
                return HttpResponse("Access to the website is forbidden. Contact the website owner for permission.")
            else:
                return HttpResponse(f"Failed to fetch the URL: {url}, Status Code: {response.status_code}")

        except Exception as e:
            return HttpResponse(f"An error occurred: {str(e)}")

    return render(request, 'your_template.html')


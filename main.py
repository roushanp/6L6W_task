import requests
import pandas as pd

Name = []
Project = []
Organization = []

class gsoc:
    def __init__(self, page):
        self.page = 1
        self.pages = page

    def set_url(self):
        return f"https://summerofcode.withgoogle.com/api/program/current/project/?page={self.page}&page_size=20"

    def make_request(self):
        url = self.set_url()
        return requests.request("Get", url)

    def get_data(self):
        self.data = self.make_request().json()

    def scrap(self):
        for page in range(1, self.pages):
            self.page = page
            self.make_request()
            self.get_data()
            for a in self.data['results']:
                name = a['student']['display_name']
                organization = a['organization']['name']
                project = a['title']
                Name.append(name)
                Organization.append(organization)
                Project.append(project)

    def make_csv(self):
        self.scrap()
        df = pd.DataFrame({'Name': Name, 'Organization': Organization, 'Project': Project})
        df.to_csv('gsoc2021.csv', index=False, encoding='utf-8')


if __name__ == "__main__":
    my = gsoc(66)
    my.make_csv()

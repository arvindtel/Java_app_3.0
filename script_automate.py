import requests

def upload_to_jfrog(source_file, jfrog_repo_url, username, password):
    # Read the file content
    with open(source_file, "rb") as file:
        file_content = file.read()

    # Upload file to JFrog repository
    upload_url = f"{jfrog_repo_url}/{source_file}"
    response = requests.put(upload_url, auth=(username, password), data=file_content)
    response.raise_for_status()

def download_from_jfrog(file_name, download_path, jfrog_repo_url, username, password):
    # Download file from JFrog repository
    download_url = f"{jfrog_repo_url}/{file_name}"
    response = requests.get(download_url, auth=(username, password))
    response.raise_for_status()

    # Save the file to the download path
    with open(download_path, "wb") as file:
        file.write(response.content)

# Specify the source WAR file to upload, JFrog repository URL, username, and password
source_war_file = "/target/*.war"
jfrog_repository = "http://52.53.228.138:8082/artifactory/libs-snapshot-local/"
username = "admin"
password = "Welcome@109"

# Upload WAR file to JFrog repository
upload_to_jfrog(source_war_file, jfrog_repository, username, password)

# Specify the WAR file name to download, download path, JFrog repository URL, username, and password
war_file_name = "kubernetes-configmap-reload-0.0.1-SNAPSHOT.war"
download_destination = "/opt/"

# Download WAR file from JFrog repository
download_from_jfrog(war_file_name, download_destination, jfrog_repository, username, password)

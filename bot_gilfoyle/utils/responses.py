import random
import datetime
import re

def get_document_link(keyword):
    """Return a link to documentation or resources based on the keyword."""
    links = {
        'linux': 'https://www.kernel.org/doc/html/latest/',
        'networking': 'https://www.networkworld.com/category/networking/',
        'ip': 'https://www.arin.net/knowledge/ipaddress/',
        'firewall': 'https://www.cio.com/article/262472/security-what-is-a-firewall.html',
        'ssh': 'https://www.ssh.com/academy/ssh',
        'server': 'https://www.redhat.com/en/topics/management/what-is-a-server',
        'virtualization': 'https://www.vmware.com/topics/what-is-virtualization',
        'proxmox': 'https://www.proxmox.com/en/proxmox-ve',
        'docker': 'https://docs.docker.com/get-started/',
        'kubernetes': 'https://kubernetes.io/docs/home/',
        'ansible': 'https://docs.ansible.com/ansible/latest/index.html',
        'git': 'https://git-scm.com/doc',
        'python': 'https://docs.python.org/3/',
        'powershell': 'https://docs.microsoft.com/en-us/powershell/',
        'script': 'https://docs.python.org/3/tutorial/index.html',
        'it-connect': 'https://www.it-connect.fr/',
        'cisco': 'https://www.cisco.com/c/en/us/support/index.html',
        'windows server': 'https://docs.microsoft.com/en-us/windows-server/',
        'pfsense': 'https://docs.netgate.com/pfsense/en/latest/',
        'wireguard': 'https://www.wireguard.com/docs/',
        'glpi': 'https://glpi-project.org/documentation/'
    }
    return links.get(keyword.lower())

def extract_doc_page_reference(input_text):
    """Extract page number and documentation name from input text."""
    match = re.search(r'page\s+(\d+)\s+de\s+(\S+)', input_text, re.IGNORECASE)
    if match:
        page_number = match.group(1)
        doc_name = match.group(2)
        return page_number, doc_name
    return None, None

def get_gilfoyle_response(input_text, user_id, last_insult):
    current_time = datetime.datetime.now()
    if user_id in last_insult and (current_time - last_insult[user_id]).seconds < 30:
        return "Je t'ai déjà insulté il y a moins de 30 secondes. Je ne vais pas gaspiller mon énergie à répéter."

    # List of insults
    insults = [
        "Tu es une véritable déception.",
        "Il est clair que tu n'as aucune idée de ce que tu fais.",
        "C'est fascinant de voir à quel point tu peux être incompétent.",
        "Ton niveau de compétence est vraiment minable.",
        "Si l'idiotie était une compétence, tu serais un génie.",
        "Ta présence ici est une perte de temps.",
        "Même un hamster serait plus utile dans ce rôle.",
        "Il est difficile de croire que quelqu'un puisse être aussi inutile.",
        "Je ne suis pas sûr de ce qui est pire : ton ignorance ou ton arrogance.",
        "Tu es la raison pour laquelle le bouton 'mute' a été inventé."
    ]

    insult = random.choice(insults)
    last_insult[user_id] = current_time
    return insult

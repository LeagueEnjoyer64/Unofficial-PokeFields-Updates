import base64,hashlib,json,os,pathlib,urllib.request,re,html,shutil
root='https://api.github.com/repos/'+os.environ['GITHUB_REPOSITORY']
headers={'Authorization':'Bearer '+os.environ['GH_TOKEN'],'Accept':'application/vnd.github+json'}
def api(path,method='GET',body=None):
    request=urllib.request.Request(root+path,headers=headers,method=method,data=json.dumps(body).encode() if body is not None else None)
    with urllib.request.urlopen(request) as r:return json.load(r)
m=json.loads(pathlib.Path('payload/manifest.json').read_text())
with open(m['file'],'wb') as output:
    for part in m['parts']:
        if part.get('remote'):
            page=urllib.request.urlopen('https://www.mediafire.com/file/33bcg73fttklebm/HD_Battle_Sprites.mod/file',timeout=60).read().decode()
            url=html.unescape(re.search(r'https://download[^\s"<>]+',page)[0])
            digest=hashlib.sha256();count=0
            with urllib.request.urlopen(url,timeout=180) as response:
                while chunk:=response.read(4*1024*1024):
                    output.write(chunk);digest.update(chunk);count+=len(chunk)
            assert count==part['bytes'] and digest.hexdigest()==part['sha256']
            continue
        data=(pathlib.Path('payload')/part['file']).read_bytes()
        assert hashlib.sha256(data).hexdigest()==part['sha256']
        output.write(data)
apk=pathlib.Path(m['file'])
assert apk.stat().st_size==m['bytes']
assert hashlib.file_digest(apk.open('rb'),'sha256').hexdigest()==m['sha256']
release=next((r for r in api('/releases?per_page=100') if r['tag_name']==m['tag']),None)
if release is None:
    release=api('/releases','POST',{'tag_name':m['tag'],'target_commitish':os.environ['GITHUB_SHA'],'name':'PokeFields HD Mods Test - Bundled and enabled (DRAFT)','body':pathlib.Path('README.md').read_text()+'\nSHA256: '+m['sha256'],'draft':True,'prerelease':True,'make_latest':'false'})
assert release['draft'] is True and release['prerelease'] is True
assert not any(a['name']==m['file'] for a in api('/releases/'+str(release['id'])+'/assets'))
url=release['upload_url'].split('{')[0]+'?name='+m['file']
request=urllib.request.Request(url,method='POST',headers={**headers,'Content-Type':'application/vnd.android.package-archive'},data=apk.read_bytes())
with urllib.request.urlopen(request,timeout=900) as r:asset=json.load(r)
assert asset['size']==m['bytes'] and asset['state']=='uploaded'
assert asset.get('digest')=='sha256:'+m['sha256']
receipt={'url':release['html_url'],'draft':True,'prerelease':True,'asset':asset,'sha256':m['sha256']}
api('/contents/upload-result.json','PUT',{'message':'Record verified draft APK upload','branch':os.environ['GITHUB_REF_NAME'],'content':base64.b64encode(json.dumps(receipt,indent=2).encode()).decode()})
print('Verified draft upload:',release['html_url'],flush=True)

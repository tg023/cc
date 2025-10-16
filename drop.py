import dropbox


ACCESS_TOKEN = "sl.u.AGBwey2nZyh4opywVVA72DFwVIdcEBlf29pWH55OtiwmVedroHe9LpEb6_BU3vHO8TIb7UdPGLTFwHZq-vBVufW1MgfalE1rGsYP_XCM-d65nTAkKTdGn0TEER0fFcGhsnpWWQWELFNzMZMt4H58VhTo85LRAORbySrlgEvFUxOPRvoGJEyy6t22f2swER9quHCJaYBcrhn0E9cjjysj7teOd5dl6Cuua2Ayua6Pe-ckrrRxwC1U9_IHmj1Sm4pd-HoRXUcStaihGOlIZ72NX31_2TDnhh-adUf9h3q5XqsTE42N_NTMrpLaWZ3EP-bXQbn9XYv4acHDtYXlkbMPNsVH25ei39b3LIUpI_OWxxpU7UTtHh2qBbzH8RuA-vnZM3K4KVkLXZUU0CYTWSfcVU0GerbEPgwHELgl1Htf793bfew_5JGXHIXRHWdP9e0xy6D_jATKWaKhu41oOJmkAOmeHxCs7o2DgDeBo2IHF-R9-tUvJ_tkcwqhADCTQ0m2mn0FfxSA9k8_hNdlE2xLVD9cy1JlXYHbq9fh5bGPvTrjyiuGq44pVhANUVUmq11WI0jg3P8tGj_0osEgtcu0RpuI39jIU4jU-XaASP5PCFkCbftVSA4P8nK0f-LQAlq7Kin5FdOen7ki-UuAIe0JIFQStmhBpRxGRg0_XGsH7ycSYlujC8uq3YUDa3iUaFr3VwHNoRIhHRIPugWtrvkc40AOcdksQYHqLVhRNlrtliZ6OefnhBO6zHTjP0DpX5vUKKwQhJst76iIGQZjMH1ZCYyqA-PO0XJC000fI7fTj3xkAIxoYfd2mL9KsXbHn2ttYUeoWXIATk7LazSUqOAavtPk7ElIaq50sACQyL1JHhy31Jl_pxiZ1Sgkc-Lg1MCc97vSJOCv2X3FrazAVuEzsuXR1k2QP3HhXyHZTw_dB1FMpniuogGTma6lcciGz0i04OblMdLNBX_4IKMso0WtxCvQ_C9uw0vibEgz136IjFy3QEIGIxxhCBW6CuEz_LdTmHQIUc4kfbLp4f2RXBxR1GB1kEUzhrBCQ_ofLDAdAl20kFCL8g_e6p_1hmKMZE1RofyFCPoJYV3ekirsfMW2inGXoXCMwk7uP6GzZ26JglEeNYNSaApKzU0oHHS_eVrXgswcQZMYYZCkKpS4qgChmQ11hwe5kSfiliEwIp9OEXW06-D3iEXBe-o2qxT-HHjp-tM1FmqXqvJJTTE1jmP_u1bmYX0FILSnN_xtVTGhH7IHBRzAxAzCVIog6t922JDLj2pbDXZn4jLzgAihrnX-4wNipR923Ss1-BWUd-8CfBu3kb370FxJbPwqENLzqB_BwcLI3MeiV74_vRWwQxHAsXng52PySqll2MXO5PeIF7chk9rpSA7NFkNbZ5ap5FdulPlguT6bkTyV0aj2oCMo4ljB"


dbx = dropbox.Dropbox(ACCESS_TOKEN)


def upload_file(local_path, dropbox_path):
    with open(local_path, 'rb') as f:
        dbx.files_upload(f.read(), dropbox_path, mode=dropbox.files.WriteMode.overwrite)
    print(f"Uploaded '{local_path}' to Dropbox as '{dropbox_path}'")


def download_file(dropbox_path, local_path):
    metadata, res = dbx.files_download(path=dropbox_path)
    with open(local_path, 'wb') as f:
        f.write(res.content)
    print(f"Downloaded '{dropbox_path}' from Dropbox to '{local_path}'")


if __name__ == "__main__":
    
    upload_file("/content/image.jpg", "/try.jpg")


    
    download_file("/try.jpg", "/content/downloadedimage.jpg")
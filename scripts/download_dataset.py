from huggingface_hub import hf_hub_download

file_path = hf_hub_download(
    repo_id="kairosmaterial/MAG188",
    filename="MAG188-SAMPLE/mag188_sample_trajectories.extxyz",
    repo_type="dataset"
)

print(file_path)
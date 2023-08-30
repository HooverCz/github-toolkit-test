# job_names=$(
#     yq eval '.default.workflows[].name' "deploy_spec.json" | tr -d '"'
# )

job_names=$(
    yq --output-format=p eval '.default.workflows[].name' "deploy_spec.json"
)
echo $job_names

job_ids=$(
    yq eval '.default.workflows[].job_id' "deploy_spec.json"
)
echo $job_ids
# for job in $job_names; do
#     dbx_launch_logs="$(
#         dbx launch  $job
#     )"
#     echo "$dbx_launch_logs"
#     # run_id=$(echo "$dbx_launch_logs" | grep -oP "(?<=run/)\d+")
#     run_id=$(echo "$input" | grep -o '/run/[0-9]\+' | cut -d'/' -f3)
# done

rm -rf out_user_by_country
#
hadoop jar /opt/hadoop/hadoop-streaming.jar \
    -D mapreduce.job.reduces=1 \
    -files total_users_hits_mapper.py,user_by_country_reducer.py,IP2LOCATION-LITE-DB1.CSV -input access.log.2017-03-13 -output out_user_by_country/ \
    -mapper ./total_users_hits_mapper.py \
    -reducer ./user_by_country_reducer.py


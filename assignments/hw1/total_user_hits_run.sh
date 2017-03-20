hadoop --config conf.empty \
            jar /opt/cloudera/parcels/CDH/lib/hadoop-mapreduce/hadoop-streaming.jar \
            -files total_users_hits_mapper.py,total_users_hits_reducer.py \
            -input access.log.2017-03-13 \
            -output out_user_hits/ \
            -mapper ./total_users_hits_mapper.py \
            -reducer ./total_users_hits_reducer.py

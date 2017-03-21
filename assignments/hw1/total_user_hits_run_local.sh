hadoop --config conf.empty \
            jar /opt/cloudera/parcels/CDH/lib/hadoop-mapreduce/hadoop-streaming.jar \
            -files total_user_hits_mapper.py,total_user_hits_reducer.py \
            -input access.log.2017-03-17 \
            -output out_user_hits/ \
            -mapper ./total_user_hits_mapper.py \
            -reducer ./total_user_hits_reducer.py

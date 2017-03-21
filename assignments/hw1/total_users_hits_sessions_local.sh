rm -rf out_users_hits_sessions
# secondary sort
hadoop --conf conf.empty jar /opt/hadoop/hadoop-streaming.jar \
    -D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator \
    -D mapred.text.key.comparator.options=-k1,2 \
    -D stream.num.map.output.key.fields=2 \
    -D mapred.text.key.partitioner.options=-k1,1 \
    -D mapreduce.job.reduces=1 \
    -files total_users_hits_mapper.py,total_users_hits_reducer.py -input access.log.2017-03-13 -output out_users_hits-sessions/ \
    -mapper ./total_users_hits_mapper.py \
    -reducer ./total_users_hits_reducer.py \
    -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner


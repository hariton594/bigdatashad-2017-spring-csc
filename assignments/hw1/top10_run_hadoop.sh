# step 1
hadoop jar /opt/hadoop/hadoop-streaming.jar \
    -files top10_mapper.py,top10_reducer.py -input access.log.2017-03-13 -output out_top10_tmp \
    -mapper ./top10_mapper.py \
    -reducer ./top10_reducer.py

# sort
hadoop jar /opt/hadoop/hadoop-streaming.jar \
-D mapreduce.job.reduces=1 \
    -D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator \
    -D mapred.text.key.comparator.options=-nr \
    -files inverse.py -input out_top10_tmp/ -output out_top10/ \
    -mapper inverse.py \
    -reducer inverse.py


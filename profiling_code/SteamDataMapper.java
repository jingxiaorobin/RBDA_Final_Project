
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;
import java.io.*;
import java.util.*;
import java.lang.*;
import java.util.regex.*;
public class SteamDataMapper
extends Mapper<LongWritable, Text, Text, Text> {
@Override
  public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
    String line = value.toString();
    String [] arrVal = line.split(",");
    String rating = "";

    for (int i = 0; i < arrVal.length; i++){
      if (arrVal[i].contains("%")) {
        rating = arrVal[i];
        break;
      }
    }
    context.write(new Text(arrVal[1].replaceAll("\"", "")), new Text(rating));

  }
}

import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { TypeOrmModule } from '@nestjs/typeorm'

@Module({
  imports: [TypeOrmModule.forRoot({
    type: 'postgres',
    host: 'localhost',
    port: 5432,
    username: 'your_db_user',
    password: 'your_db_password',
    database: 'workers_platform',
    autoLoadEntities: true,
    synchronize: true, // set false in production
  }),],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule { }

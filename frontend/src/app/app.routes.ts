import { Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { UploadComponent } from './upload/upload.component';
import { AnalyzeComponent } from './analyze/analyze.component';

export const routes: Routes = [
  { path: '', component: HomeComponent },
  {path:'upload', component: UploadComponent},
  {path:'analyze', component: AnalyzeComponent},
  { path: '**', redirectTo: '' }
];
